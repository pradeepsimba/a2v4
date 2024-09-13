def hourlytarget(request):
    locations = userProfile.objects.filter(
        Q(location__isnull=False) & ~Q(location='')).values('location').distinct()
    if request.method == 'POST':
        scope = request.POST.get('scope')
        location = request.POST.get('location')
        date = request.POST.get('date')
        key = request.POST.get('key')

        role = Q()
        if not scope == 'All':
            role = Q(targetfor=scope)

        locprod = Q()
        loctarget = Q()
        if not location == 'All':
            locprod = Q(created_by__location=location)
            loctarget = Q(targetempid__location=location)

        prod_Date = Q(end_time__date=date)

        table_names = []
        if scope == 'DA1' or scope == 'All':
            table_names.extend(['l1_production'])

        if scope == 'QA' or scope == 'All':
            table_names.extend(['l4_production'])

        querysets = []
        for table_name in table_names:
            queryset = globals()[table_name].objects.filter(prod_Date, locprod).values(
                date=F('created_at__date'),
                empid=F('created_by__username'),
                empname=F('created_by__userprofile__employeeName')
            ).annotate(
                source_table=Value(str(table_name), output_field=CharField()),
                crtdhr=ExtractHour('end_time'),
                count=Count('created_by_id'),
                filename=F('qid__baseid__filename'),
            ).exclude(qid__status__in=['hold', 'deleted'])
            querysets.append(queryset)
        productionhourly = list(chain(*querysets))

        targetdata = targetsetting.objects.filter(role, loctarget, target_date__date=date).values(
            'target', 'targetempid__userprofile__location', empid=F('targetempid__username'), empname=F('targetempid__userprofile__employeeName'))
        qsifttime = ShiftTime.objects.filter(created_at__date=date).annotate(
            shifttime=ExtractHour(Sum(F('endtime') - F('starttime')))
        ).values('shifttime', empid=F('user__username'))

        df_prodhoure = pd.DataFrame(productionhourly)
        df_targetdata = pd.DataFrame(targetdata)
        df_sifttime = pd.DataFrame(qsifttime)
        if not df_prodhoure.empty and not df_targetdata.empty:
            mrgd = pd.merge(df_prodhoure, df_targetdata, on=[
                            'empid', 'empname'], how='outer')
            mrgd = mrgd.pivot_table(index=['empid', 'empname', 'filename', 'targetempid__userprofile__location', 'target'],
                                    columns='crtdhr',
                                    values='count',
                                    fill_value=0).reset_index()

            if not df_sifttime.empty:
                droplist = ['houretarget', 'shifttime']
                mrgd = pd.merge(mrgd, df_sifttime, on='empid',
                                how='left').fillna(0)

                mrgd['houretarget'] = mrgd.apply(lambda row: round(
                    int(row['target']) / 8, 2), axis=1).astype(int)

                # mrgd['houretarget'] = mrgd.apply(lambda row: round((int(row['target']) * getcount(row['filename'])) / 100,2), axis=1)
                # mrgd['houretarget'] = mrgd.apply(lambda row: round(int(row['houretarget']) / int(row['shifttime']) if int(row['shifttime']) != 0 else int(11),1), axis=1)
            else:
                droplist = ['houretarget']
                mrgd['houretarget'] = mrgd.apply(lambda row: round(
                    int(row['target']) / 8, 2), axis=1).astype(int)

                # mrgd['houretarget'] = mrgd.apply(lambda row: round((int(row['target']) * getcount(row['filename'])) / 100,2), axis=1)
                # mrgd['houretarget'] = mrgd.apply(lambda row: round(int(row['houretarget']) / int(11),1), axis=1)

            tablecolumn = ['empid', 'filename', 'empname',
                           'targetempid__location', 'target', 'Hourly Target']
            mrgd = mrgd.rename(columns=lambda x: str(
                x) if x not in tablecolumn else x)
            mrgd = mrgd.fillna(0)
            mrgd.insert(mrgd.columns.get_loc('target') + 1,
                        'Hourly Target', mrgd['houretarget'])
            mrgd = mrgd.drop(columns=droplist)

            # mrgd = mrgd[tablecolumn]
            mrgd = mrgd.rename(columns=rnmhourlycolumn)
            mrgd.index = np.arange(1, len(mrgd) + 1)

            if key == 'Download':
                lable = 'Hourly_Report'
                response = HttpResponse(
                    content_type='text/csv; charset=utf-8-sig')
                response['Content-Disposition'] = 'attachment; filename="' + lable + \
                    str(timezone.now().date())+'".csv"'
                mrgd.to_csv(path_or_buf=response,
                            index=False, encoding='utf-8-sig')

                return response
            else:
                mrgd = mrgd.to_html().replace('<table border="1" class="dataframe">', '<table id="dftable" class="table table-hover">').replace('<thead>',
                                                                                                                                                '<thead class="thead-light align-item-center">').replace('<tr style="text-align: right;">', '<tr>').replace('<th></th>', '<th>S.No</th>')
                return render(request, 'pages/hourly_target.html', {'houretarget': mrgd, 'locations': locations,  'scope': scope, 'location': location, 'date': date, 'key': key})
        else:
            return render(request, 'pages/hourly_target.html', {'locations': locations, 'date': date, 'scope': scope, 'location': location, 'Alert': json.dumps({'type': 'Info', 'message': 'No records'})})
    else:
        return render(request, 'pages/hourly_target.html', {'locations': locations})
