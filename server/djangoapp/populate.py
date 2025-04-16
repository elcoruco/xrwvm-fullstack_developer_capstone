from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology"},
        {"name": "Mercedes", "description": "Great cars. German technology"},
        {"name": "Audi", "description": "Great cars. German technology"},
        {"name": "Kia", "description": "Great cars. Korean technology"},
        {"name": "Toyota", "description": "Great cars. Japanese technology"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(
            CarMake.objects.create(
                name=data['name'], description=data['description']
            )
        )

    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
        {
            "name": "Pathfinder",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[0],
            "price": 45000.00
        },
        {
            "name": "Qashqai",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[0],
            "price": 33000.00
        },
        {
            "name": "XTRAIL",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[0],
            "price": 38000.00
        },
        {
            "name": "A-Class",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[1],
            "price": 55000.00
        },
        {
            "name": "C-Class",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[1],
            "price": 65000.00
        },
        {
            "name": "E-Class",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[1],
            "price": 85000.00
        },
        {
            "name": "A4",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[2],
            "price": 58000.00
        },
        {
            "name": "A5",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[2],
            "price": 62000.00
        },
        {
            "name": "A6",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[2],
            "price": 75000.00
        },
        {
            "name": "Sorrento",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[3],
            "price": 42000.00
        },
        {
            "name": "Carnival",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[3],
            "price": 45000.00
        },
        {
            "name": "Cerato",
            "type": "Sedan",
            "year": 2023,
            "car_make": car_make_instances[3],
            "price": 26000.00
        },
        {
            "name": "Corolla",
            "type": "Sedan",
            "year": 2023,
            "car_make": car_make_instances[4],
            "price": 25000.00
        },
        {
            "name": "Camry",
            "type": "Sedan",
            "year": 2023,
            "car_make": car_make_instances[4],
            "price": 35000.00
        },
        {
            "name": "Kluger",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[4],
            "price": 52000.00
        },
        # Add more CarModel instances as needed
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'],
            car_make=data['car_make'],
            type=data['type'],
            year=data['year'],
            price=data['price']
        )
        