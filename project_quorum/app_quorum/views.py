import csv
from django.shortcuts import render

from . import models


def home(request):
    legislators_dropdown_data = list()
    with open('project_quorum/app_quorum/data/legislators.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            legislator = models.Legislators.objects.create(id_legislator=row['id'], name=row['name'])
            legislators_dropdown_data.append(legislator.name)
    legislators_dropdown_data.sort()

    bills_dropdown_data = list()
    with open('project_quorum/app_quorum/data/bills.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bill = models.Bills.objects.create(id_bill=row['id'], title=row['title'], primary_sponsor=row['sponsor_id'])
            bills_dropdown_data.append(bill.title)
    bills_dropdown_data.sort()
    
    return render(request, 'home.html', {'legislators_dropdown_data': legislators_dropdown_data, 'bills_dropdown_data': bills_dropdown_data})


def legislators(request):
    input_legislator_name = request.POST.get('legislator_name_selection')
    id_legislator=None
    vote_yes = 0
    vote_no = 0

    with open('project_quorum/app_quorum/data/legislators.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            legislator = models.Legislators.objects.create(id_legislator=row['id'], name=row['name'])
            if legislator.name == input_legislator_name:
                id_legislator = legislator.id_legislator
                break
    
    with open('project_quorum/app_quorum/data/vote_results.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            vote_result = models.VotesResults.objects.create(id_results=row['id'], id_legislator=row['legislator_id'], id_vote=row['vote_id'], vote_type=row['vote_type'])
            if vote_result.id_legislator == id_legislator:
                if int(vote_result.vote_type) == 1:
                    vote_yes += 1
                else:
                    vote_no += 1
    
    data_return = {'id_legislator': id_legislator, 'input_legislator_name': input_legislator_name, 'vote_yes': vote_yes, 'vote_no': vote_no}

    return render(request, 'legislators.html', data_return)
        
        
def bills(request):
    input_bill_title = request.POST.get('bill_title_selection')
    vote_yes = 0
    vote_no = 0
    
    with open('project_quorum/app_quorum/data/bills.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bill = models.Bills.objects.create(id_bill=row['id'], title=row['title'], primary_sponsor=row['sponsor_id'])
            if bill.title == input_bill_title:
                break

    with open('project_quorum/app_quorum/data/votes.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        id_votes_list = list()
        for row in reader:
            vote = models.Votes.objects.create(id_vote=row['id'], id_bill=row['bill_id'])
            if vote.id_bill == bill.id_bill:
                id_votes_list.append(vote.id_vote)    
    
    with open('project_quorum/app_quorum/data/vote_results.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            vote_result = models.VotesResults.objects.create(id_results=row['id'], id_legislator=row['legislator_id'], id_vote=row['vote_id'], vote_type=row['vote_type'])
            if vote_result.id_vote in id_votes_list:
                if int(vote_result.vote_type) == 1:
                    vote_yes += 1
                else:
                    vote_no += 1

    with open('project_quorum/app_quorum/data/legislators.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        legislator_name = 'Legislator not registered'
        for row in reader:
            legislator = models.Legislators.objects.create(id_legislator=row['id'], name=row['name'])
            if legislator.id_legislator == bill.primary_sponsor:
                legislator_name = legislator.name
                break
        
    data_return = {'id_bill': bill.id_bill, 'bill_title': bill.title, 'vote_yes': vote_yes, 'vote_no': vote_no, 'primary_sponsor': legislator_name}
    
    return render(request, 'bills.html', data_return)