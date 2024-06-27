from django.urls import path
from app.views import *

# Add more URLs as needed

urlpatterns = [

    ######################### Productions ####################################
    path('productionl1/', loneproductionView, name='productionl1'),
    path('productionl4/', lfourproductionView, name='productionl4'),

    ######################### File Management ################################
    path('upload/', uploadView, name='upload'),
    path('fileMamagement/', fileMamagement, name='fileMamagement'),
    path('fileDownload/<str:batchid>/<str:filename_form>/', fileDownload, name='fileDownload'),
    path('miniFileDownload/', miniFileDownload, name='miniFileDownload'),

    path('sample_file_download/', SampleFileDownloadView,
         name='sample_file_download'),

    ######################### OutPut Download ########################################
    path('outputDownload/', outputDownload, name='outputDownload'),
    path('ConsolidateOutput/', ConsolidateOutput, name='ConsolidateOutput'),

    ######################## User Management ##################################
    path('userTable/', userTable, name='userTable'),
    path('UserManagement/', UserManagement, name='UserManagement'),
    path('OverAllRole/', OverAllRole, name='OverAllRole'),
    path('logout/', app_logOut, name='logout'),

    ######################## Tracking ##################################
    path('target/', target, name='target'),
    path('save_table_data/', save_table_data, name='save_table_data'),
    path('batchwisetracking/', batchwisetracking, name='batchwisetracking'),
    path('userwisetracking/', userwisetracking, name='userwisetracking'),
    path('hourly/', hourlytarget, name='hourlytarget'),
    path('qualityreport/', qualityreport, name='qualityreport'),
    path('UT_Report/', ut_report, name='ut_report'),
    path('AHT_Report/', aht_report, name='aht_report'),
    path('iaa/', iaa, name='iaa'),

    path('CK_Report/', ck_report, name='ck_report'),

    path('resetuser/', resetuser, name='resetuser'),

    ################### Project Management #####################################

    path('project_management/',project_management,name='project_management')

]
