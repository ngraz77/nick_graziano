def make_car(manufacturer, model, **features):
    car = {
        "manufacturer": manufacturer,
        "model": model
    }
    car.update(features)
    return car

my_car = make_car("Subaru", "Nissan", color="green", tow_package=True)

print(my_car)