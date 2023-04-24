from django.shortcuts import render
from django.views import View
from .models import Predictions
from . import bj, es, shls, you


class Home(View):
    def get(self, request, *args, **kwargs):
        predictions = Predictions.objects.last()
        if predictions != None:
            pred = {
                "stock": predictions.stock,
                "open": predictions.open_p, 
                "high": predictions.high, 
                "low": predictions.low, 
                "close": predictions.close}
            pattern = predictions.pattern
            return render(request, "main/main.html", {"pred": pred, "pattern": pattern})
        else:
            return render(request, "main/main.html")
    
    def post(self, request, *args, **kwargs):
        option = request.POST["option"]
        if option == "bj":
            pred = bj.alert()
            pattern = bj.pattern()
            Predictions.objects.create(
                pattern=pattern, open_p=pred["open"],
                high=pred["high"], low=pred["low"],
                close=pred["close"], stock=option.upper()
                )
        elif option == "es":
            pred = es.alert()
            pattern = es.pattern()
            Predictions.objects.create(
                pattern=pattern, open_p=pred["open"],
                high=pred["high"], low=pred["low"],
                close=pred["close"], stock=option.upper()
                )
        elif option == "shls":
            pred = shls.alert()
            pattern = shls.pattern()
            Predictions.objects.create(
                pattern=pattern, open_p=pred["open"],
                high=pred["high"], low=pred["low"],
                close=pred["close"], stock=option.upper()
                )
        else:
            pred = you.alert()
            pattern = you.pattern()
            Predictions.objects.create(
                pattern=pattern, open_p=pred["open"],
                high=pred["high"], low=pred["low"],
                close=pred["close"], stock=option.upper()
                )
        pred["stock"] = option.upper()
        return render(request, "main/main.html", {"pred": pred, "pattern": pattern})
