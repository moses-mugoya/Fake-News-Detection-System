import pickle
from django.shortcuts import render
from .forms import FakeNewsForm


def fakenews(request):
    prediction = ""
    prob = ""
    mydata = ""
    if request.method == 'POST':
        fakeform = FakeNewsForm(request.POST)
        if fakeform.is_valid():
            mydata = fakeform.cleaned_data['text']
            load_model = pickle.load(open('final_model.sav', 'rb'))
            prediction = load_model.predict([mydata])
            prob = load_model.predict_proba([mydata])
            
            if prediction[0] != "":
                prediction = prediction[0]

            if prob[0][1] != "":
                prob = prob[0][1]

    else:
        fakeform = FakeNewsForm()
    return render(request, 'fake/fake.html', {'prediction': prediction, 'prob': prob, 'fakeform': fakeform, 'mydata': mydata})




