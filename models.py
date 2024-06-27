import json
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from django.db.models.functions import Now

# # Create your models here.

# class Project(models.Model):
#     user = models.ForeignKey(
#         'userProfile', null=True, blank=True, on_delete=models.RESTRICT)
#     profject_name =  models.CharField(max_length=150, blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     created_by = models.ForeignKey(
#         'userProfile', null=True, blank=True, on_delete=models.RESTRICT, related_name='Project_created_by')

class userProfile(models.Model):
    employeeID = models.CharField(
        max_length=255, blank=True, null=True, unique=True)
    employeeName = models.CharField(max_length=150, blank=True, null=True)
    reporting = models.CharField(max_length=150, blank=True, null=True)
    location = models.CharField(max_length=150, blank=True, null=True)
    language = models.TextField(max_length=150, blank=True, null=True)
    prodStart_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Roles(models.Model):
    userprofile = models.ForeignKey(
        userProfile, null=True, blank=True, on_delete=models.RESTRICT)
    role = models.CharField(max_length=150, blank=True, null=True)
    created_by = models.ForeignKey(
        userProfile, null=True, blank=True, on_delete=models.RESTRICT, related_name='Role_created_by')

    class Meta:
        unique_together = ('role', 'userprofile')

class Languages(models.Model):
    language = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        userProfile, null=True, blank=True, on_delete=models.RESTRICT, related_name='Language_created_by')

class Location(models.Model):
    location = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        userProfile, null=True, blank=True, on_delete=models.RESTRICT, related_name='Location_created_by')


class ShiftTime(models.Model):
    userprofile = models.ForeignKey(
        userProfile, null=True, blank=True, on_delete=models.RESTRICT)
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    created_by = models.ForeignKey(
        userProfile, null=True, blank=True, on_delete=models.RESTRICT, related_name='ShiftTime_created_by')

class basefile(models.Model):
    batch_name = models.CharField(max_length=255, blank=True, null=True)
    filename = models.CharField(max_length=150, blank=True, null=True,unique=True)
    language = models.CharField(max_length=150, blank=True, null=True)
    created_by = models.ForeignKey(
        userProfile, null=True, blank=True, on_delete=models.CASCADE,related_name = 'basefile')
    created_at = models.DateTimeField(auto_now_add=True, blank=True)    
    class Meta:
        unique_together = ('batch_name', 'filename')

class raw_data(models.Model):
    baseid = models.ForeignKey(basefile,null=True,blank=True,on_delete=models.CASCADE)
    
    id_value = models.CharField(max_length=1255, blank=True, null=True)
    question = models.TextField(blank=True, null=True)
    asin = models.CharField(max_length=1255, blank=True, null=True)
    title = models.CharField(max_length=1255, blank=True, null=True)
    product_url = models.CharField(max_length=1255, blank=True, null=True)
    imagepath = models.CharField(max_length=1255, blank=True, null=True)
    evidence = models.TextField(blank=True, null=True)
    answer_one = models.TextField(blank=True, null=True)
    answer_two = models.TextField(blank=True, null=True)
    
    nile_rq = models.TextField(blank=True, null=True)
    
    # not_picked,picked,completed
    l1_status = models.CharField(
        default='not_picked', max_length=255, blank=True, null=True)
    # not_picked,picked,completed

    # not_picked,picked,completed
    l4_status = models.CharField(
        default='not_picked', max_length=255, blank=True, null=True)



    l1_emp = models.ForeignKey(
        userProfile, null=True, blank=True, on_delete=models.RESTRICT, related_name='l1_user_data')

    l4_emp = models.ForeignKey(
        userProfile, null=True, blank=True, on_delete=models.RESTRICT, related_name='l4_user_data')
    
    l1_prod = models.ForeignKey(
        'l1_production', null=True, blank=True, on_delete=models.CASCADE, related_name='l1_prodid')

    l4_prod = models.ForeignKey(
        'l4_production', null=True, blank=True, on_delete=models.CASCADE, related_name='l4_prodid')

    status = models.CharField(
        default='processing', max_length=255, blank=True, null=True)  # onhold ready

    l1_loc = models.CharField(max_length=150, blank=True, null=True)


    # created_by = models.ForeignKey(
    #     userProfile, null=True, blank=True, on_delete=models.RESTRICT)

    # created_at = models.DateTimeField(auto_now_add=True, blank=True)

    # class Meta:
    #     unique_together = ('batch_name', 'id_value')

    # def __str__(self):
    #     return self.title


class l1_production(models.Model):
    qid = models.ForeignKey(
        'raw_data', null=True, blank=True, on_delete=models.CASCADE)
    
    que1 = models.CharField(max_length=855, blank=True, null=True)
    que2 = models.CharField(max_length=855, blank=True, null=True)
    que3 = models.CharField(max_length=855, blank=True, null=True)
    que4 = models.CharField(max_length=855, blank=True, null=True)

    que5_ans1 = models.CharField(max_length=855, blank=True, null=True)
    que6_ans1 = models.CharField(max_length=855, blank=True, null=True)
    que6a_ans1 = models.CharField(max_length=855, blank=True, null=True)
    que6a1_ans1 = models.CharField(max_length=855, blank=True, null=True)
    que6a2_ans1 = models.CharField(max_length=855, blank=True, null=True)
    que6a3_ans1 = models.CharField(max_length=855, blank=True, null=True)
    que6a4_ans1 = models.CharField(max_length=855, blank=True, null=True)
    que7_ans1 = models.CharField(max_length=855, blank=True, null=True)
    que8_ans1 = models.CharField(max_length=855, blank=True, null=True)
    que26_ans1 = models.CharField(max_length=855, blank=True, null=True)
    que27_ans1 = models.CharField(max_length=855, blank=True, null=True)
    que28_ans1 = models.CharField(max_length=855, blank=True, null=True)
    que28a_ans1 = models.CharField(max_length=855, blank=True, null=True)
    que28a1_ans1 = models.CharField(max_length=855, blank=True, null=True)
    que28a2_ans1 = models.CharField(max_length=855, blank=True, null=True)
    que28a3_ans1 = models.CharField(max_length=855, blank=True, null=True)
    que28a4_ans1 = models.CharField(max_length=855, blank=True, null=True)
    que29_ans1 = models.CharField(max_length=855, blank=True, null=True)

    que5_ans2 = models.CharField(max_length=855, blank=True, null=True)
    que6_ans2 = models.CharField(max_length=855, blank=True, null=True)
    que6a_ans2 = models.CharField(max_length=855, blank=True, null=True)
    que6a1_ans2 = models.CharField(max_length=855, blank=True, null=True)
    que6a2_ans2 = models.CharField(max_length=855, blank=True, null=True)
    que6a3_ans2 = models.CharField(max_length=855, blank=True, null=True)
    que6a4_ans2 = models.CharField(max_length=855, blank=True, null=True)
    que7_ans2 = models.CharField(max_length=855, blank=True, null=True)
    que8_ans2 = models.CharField(max_length=855, blank=True, null=True)
    que26_ans2 = models.CharField(max_length=855, blank=True, null=True)
    que27_ans2 = models.CharField(max_length=855, blank=True, null=True)
    que28_ans2 = models.CharField(max_length=855, blank=True, null=True)
    que28a_ans2 = models.CharField(max_length=855, blank=True, null=True)
    que28a1_ans2 = models.CharField(max_length=855, blank=True, null=True)
    que28a2_ans2 = models.CharField(max_length=855, blank=True, null=True)
    que28a3_ans2 = models.CharField(max_length=855, blank=True, null=True)
    que28a4_ans2 = models.CharField(max_length=855, blank=True, null=True)
    que29_ans2 = models.CharField(max_length=855, blank=True, null=True)

    is_status = models.TextField(blank=True, null=True)
    is_production_status = models.CharField(
        max_length=255, blank=True, null=True)

    start_time = models.DateTimeField(null=True,blank=True)
    end_time = models.DateTimeField(null=True,blank=True)
    
    created_by = models.ForeignKey(
        userProfile, null=True, blank=True, on_delete=models.CASCADE, related_name='l1_user')
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    # class Meta:
    #     unique_together = ('qid', 'created_by')

    # def __str__(self):
    #     return self.title


class l4_production(models.Model):
    qid = models.ForeignKey(
        'raw_data', null=True, blank=True, on_delete=models.CASCADE)
    
    que1 = models.CharField(max_length=855, blank=True, null=True)
    que2 = models.CharField(max_length=855, blank=True, null=True)
    que3 = models.CharField(max_length=855, blank=True, null=True)
    que4 = models.CharField(max_length=855, blank=True, null=True)

    que5_ans1 = models.CharField(max_length=855, blank=True, null=True)
    que6_ans1 = models.CharField(max_length=855, blank=True, null=True)
    que6a_ans1 = models.CharField(max_length=855, blank=True, null=True)
    que6a1_ans1 = models.CharField(max_length=855, blank=True, null=True)
    que6a2_ans1 = models.CharField(max_length=855, blank=True, null=True)
    que6a3_ans1 = models.CharField(max_length=855, blank=True, null=True)
    que6a4_ans1 = models.CharField(max_length=855, blank=True, null=True)
    que7_ans1 = models.CharField(max_length=855, blank=True, null=True)
    que8_ans1 = models.CharField(max_length=855, blank=True, null=True)
    que26_ans1 = models.CharField(max_length=855, blank=True, null=True)
    que27_ans1 = models.CharField(max_length=855, blank=True, null=True)
    que28_ans1 = models.CharField(max_length=855, blank=True, null=True)
    que28a_ans1 = models.CharField(max_length=855, blank=True, null=True)
    que28a1_ans1 = models.CharField(max_length=855, blank=True, null=True)
    que28a2_ans1 = models.CharField(max_length=855, blank=True, null=True)
    que28a3_ans1 = models.CharField(max_length=855, blank=True, null=True)
    que28a4_ans1 = models.CharField(max_length=855, blank=True, null=True)
    que29_ans1 = models.CharField(max_length=855, blank=True, null=True)

    que5_ans2 = models.CharField(max_length=855, blank=True, null=True)
    que6_ans2 = models.CharField(max_length=855, blank=True, null=True)
    que6a_ans2 = models.CharField(max_length=855, blank=True, null=True)
    que6a1_ans2 = models.CharField(max_length=855, blank=True, null=True)
    que6a2_ans2 = models.CharField(max_length=855, blank=True, null=True)
    que6a3_ans2 = models.CharField(max_length=855, blank=True, null=True)
    que6a4_ans2 = models.CharField(max_length=855, blank=True, null=True)
    que7_ans2 = models.CharField(max_length=855, blank=True, null=True)
    que8_ans2 = models.CharField(max_length=855, blank=True, null=True)
    que26_ans2 = models.CharField(max_length=855, blank=True, null=True)
    que27_ans2 = models.CharField(max_length=855, blank=True, null=True)
    que28_ans2 = models.CharField(max_length=855, blank=True, null=True)
    que28a_ans2 = models.CharField(max_length=855, blank=True, null=True)
    que28a1_ans2 = models.CharField(max_length=855, blank=True, null=True)
    que28a2_ans2 = models.CharField(max_length=855, blank=True, null=True)
    que28a3_ans2 = models.CharField(max_length=855, blank=True, null=True)
    que28a4_ans2 = models.CharField(max_length=855, blank=True, null=True)
    que29_ans2 = models.CharField(max_length=855, blank=True, null=True)

    is_status = models.TextField(blank=True, null=True) # Edited , Not
    is_production_status = models.CharField(
        max_length=255, blank=True, null=True)

    start_time = models.DateTimeField(null=True,blank=True)
    end_time = models.DateTimeField(null=True,blank=True)
    created_by = models.ForeignKey(
        userProfile, null=True, blank=True, on_delete=models.CASCADE, related_name='l4_user')
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    # class Meta:
    #     unique_together = ('qid', 'created_by')

    # def __str__(self):
    #     return self.title


class targetsetting(models.Model):
    target_date = models.DateTimeField(null=True,blank=True)
    targetempid = models.ForeignKey(userProfile,null=True,blank=True,on_delete=models.RESTRICT,related_name='targetempid')
    target = models.CharField(max_length=150,null=True,blank=True)
    targetfor = models.CharField(null=True,blank=True,max_length=150)
    created_by = models.ForeignKey(userProfile,null=True,blank=True,on_delete=models.RESTRICT,related_name='createdby')
    created_at =models.DateTimeField(auto_now_add=True,null=True,blank=True)

class QA_queue(models.Model):
    queue_date = models.DateField()
    queue_batch = models.ForeignKey(basefile,null=True,blank=True,on_delete=models.CASCADE,related_name='queue_batchid')
    queue_percentage = models.CharField(max_length=150,null=True,blank=True)
    created_by = models.ForeignKey(userProfile,null=True,blank=True,on_delete=models.RESTRICT,related_name='queue_createdby')
    created_at =models.DateTimeField(auto_now_add=True,null=True,blank=True)
 
