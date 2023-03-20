from django.shortcuts import render
from django.http import JsonResponse

import hubspot

# Create your views here.
def get_leads(request):
    try:
        client = hubspot.Client.create(access_token="pat-na1-a99cdf8e-0af7-401f-8396-6a25f8f582ee")

        all_contacts = client.crm.contacts.get_all(
            properties=["hs_lead_status", "phone", "firstname", "lastname", "hubspot_owner_id", "createdate"])
        leads = []
        for lead in all_contacts:
            leads.append(lead.to_dict())
        # return JsonResponse({'leads': leads})
        return JsonResponse(leads, safe=False)
    except:
        return JsonResponse(f'Error: Hubo un error')

