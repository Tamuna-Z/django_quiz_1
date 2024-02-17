from django.shortcuts import render

# Create your views here.

mock_db = [
    {'id': 1, 'name': 'John', 'surname': 'Doe', 'stack': 'Python', 'team_lead': 'David'},
    {'id': 2, 'name': 'Jane', 'surname': 'Smith', 'stack': 'Java', 'team_lead': 'Joana'},
    {'id': 3, 'name': 'Mike', 'surname': 'Johnson', 'stack': 'JavaScript', 'team_lead': 'Smith'},
    {'id': 4, 'name': 'Emily', 'surname': 'Williams', 'stack': 'C#', 'team_lead': 'Sarah'},
    {'id': 5, 'name': 'Alex', 'surname': 'Brown', 'stack': 'Ruby', 'team_lead': 'Philip'},
    {'id': 6, 'name': 'Sarah', 'surname': 'Miller', 'stack': 'Python', 'team_lead': 'David'},
    {'id': 7, 'name': 'Daniel', 'surname': 'Jones', 'stack': 'Java', 'team_lead': 'Joana'},
    {'id': 8, 'name': 'Sophia', 'surname': 'Davis', 'stack': 'JavaScript', 'team_lead': 'Smith'},
    {'id': 9, 'name': 'Matthew', 'surname': 'Garcia', 'stack': 'C#', 'team_lead': 'Sarah'},
    {'id': 10, 'name': 'Olivia', 'surname': 'Martinez', 'stack': 'Ruby', 'team_lead': 'Philip'},
]


def home(request):
    return render(request, 'employees/home.html')

def stack(request):
    data = []
    for i in mock_db:
        data.append({"stack": i.get("stack"), "employee": f'{i.get("name")} {i.get("surname")}'})

    return render(request, 'employees/stack.html', {"stacks": data})

def teamleads(request):
    data = []
    for i in mock_db:
        data.append({"team_lead": i.get("team_lead"), "employee": f'{i.get("name")} {i.get("surname")}'})
    return render(request, 'employees/teamleads.html', {'team_leads': data})

def employee(request):
    return render(request, 'employees/employee.html', {"employees": mock_db})

# def stack(request):
#     context = {'stacks': mock_db}
#     return render(request, 'employees/stack.html', context)
# def teamleads(request):
#     context = {'teamleads': mock_db}
#     return render(request, 'employees/teamleads.html', context)
# def employee(request):
#     context = {'employee': mock_db}
#     return render(request, 'employees/employee.html', context)



