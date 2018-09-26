# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Policy(models.Model):
    detail_id = models.IntegerField(db_column="DetailID")
    policy_no = models.CharField(max_length=90, db_column="PolicyNo")
    account_no = models.CharField(max_length=50, null=True, db_column="AccountNo")
    account_name = models.CharField(max_length=200, null=True, db_column="AccountName")
    start_date = models.DateTimeField(auto_now_add=True, null=True, db_column="StartDate")
    insurer = models.CharField(max_length=150, null=True,  db_column="Insurer")
    insurer_name = models.CharField(max_length=200, null=True, db_column="InsurerName")
    co_cos = models.SmallIntegerField(default=0, null=True, db_column="CoCos")
    insured = models.CharField(max_length=200, null=True, db_column="Insured")
    policy_type = models.SmallIntegerField(default=0, null=True, db_column="PolicyType")
    business_type = models.SmallIntegerField(default=0, null=True, db_column="BusinessType")
    commission_rate = models.FloatField(null=True, db_column="CommissionRate")
    policy_class = models.SmallIntegerField(default=0, db_column="PolicyClass")
    policy_start = models.DateTimeField(auto_now_add=True, null=True, db_column="PolicyStart")
    policy_end = models.DateTimeField(auto_now_add=True, null=True, db_column="PolicyEnd")
    renewal_date = models.DateTimeField(auto_now_add=True, null=True, db_column="RenewalDate")
    notes = models.TextField(max_length=6000, null=True, db_column="Notes")
    status = models.SmallIntegerField(default=0, null=True, db_column="Status")
    no_of_risks = models.SmallIntegerField(default=0, null=True, db_column="NoOfRisks")
    last_risk = models.SmallIntegerField(default=0, null=True, db_column="LastRisk")
    last_maintained = models.DateTimeField(auto_now_add=True, null=True, db_column="LastMaintained")
    last_user = models.CharField(max_length=50, null=True, db_column="LastUser")
    not_applied = models.FloatField(default=0,  null=True, db_column="NotApplied")
    folder_path = models.CharField(max_length=240, null=True, db_column="FolderPath")
    sum_insured = models.FloatField(default=0, null=True, db_column="SumInsured")
    premiums = models.FloatField(default=0, null=True, db_column="Premiums")
    premium_rate = models.FloatField(default=0, null=True, db_column="PremiumRate")
    adjusted_premium = models.FloatField(default=0, null=True, db_column="AdjustedPremium")
    premium_rate_type = models.IntegerField(default=0, null=True, db_column="PremiumRateType")
    t_levy = models.FloatField(default=0, null=True, db_column="TLevy")
    pc_fund = models.FloatField(default=0, null=True, db_column="PCFund")
    s_duty = models.FloatField(default=0, null=True, db_column="SDuty")
    claims = models.IntegerField(default=0, null=True, db_column="Claims")
    renewal_sums = models.TextField(max_length=600,  null=True, db_column="RenewalSums")
    renewal_info = models.TextField(max_length=600,  null=True, db_column="RenewalInfo")
    cover = models.CharField(max_length=100,  null=True, db_column="Cover")
    class_covered = models.CharField(max_length=100,  null=True, db_column="ClassCovered")

    class Meta:
        db_table = "INPolicies"

