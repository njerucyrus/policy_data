# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.http.response import HttpResponse

from insurance_data_source_api.models import Policy


# Create your views here.
def get_policy(request):
    policy = Policy.objects.get(policy_no=request.GET.get('policy_no'))
    data = {}
    if policy is not None:
        response_dict = {
            "PolicyNo": policy.policy_no,
            "AccountNo": policy.account_no,
            "AccountName": policy.account_name,
            "PolicyStart": policy.policy_start,
            "PolicyEnd": policy.policy_end,
            "RenewalDate": policy.renewal_date,
            "Insurer": policy.insurer,
            "InsurerName": policy.insurer_name,
            "PolicyType": policy.policy_type
        }

        data['data'] = response_dict
        data['status_code'] = 200
    else:
        data['data'] = {}
        data['status_code'] = 500

    return HttpResponse(json.dumps(data), content_type='application/json')
