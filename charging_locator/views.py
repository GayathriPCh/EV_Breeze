# charging_locator/views.py

from django.shortcuts import redirect, render, get_object_or_404
from .models import ChargingStation, ChargingStationReview, ChargingStationRating
from .forms import ChargingStationReviewForm
# charging_locator/views.py

def index(request):
    return render(request, 'charging_locator/index.html')

def charging_station_map(request):
    # This view remains unchanged
    return render(request, 'charging_locator/charging_station_map.html')

def carbon_footprint_calculator(request):
    if request.method == 'POST':
        # Get the form data
        distance = float(request.POST.get('distance', 0))
        vehicle_type = request.POST.get('vehicle_type')

        # Calculate the carbon footprint based on the vehicle type and distance
        if vehicle_type == 'electric_car':
            carbon_footprint = calculate_electric_car_footprint(distance)
        elif vehicle_type == 'public_transport':
            carbon_footprint = calculate_public_transport_footprint(distance)
        elif vehicle_type == 'bicycle':
            carbon_footprint = calculate_bicycle_footprint(distance)
        else:
            carbon_footprint = 0

        # Redirect to the result page with the calculated carbon footprint
        return redirect('carbon_footprint_result', carbon_footprint=carbon_footprint)
    else:
        # If the request method is not POST, render the form template
        return render(request, 'charging_locator/carbon_footprint_calculator.html')

def carbon_footprint_result(request, carbon_footprint):
    return render(request, 'charging_locator/carbon_footprint_result.html', {'carbon_footprint': carbon_footprint})

def calculate_electric_car_footprint(distance):
    # Example calculation for electric car carbon footprint
    # You can replace this with your own calculation method
    # This is just a placeholder example
    return distance * 0.05  # Assuming 0.05 kg CO2 per mile

def calculate_public_transport_footprint(distance):
    # Example calculation for public transport carbon footprint
    # You can replace this with your own calculation method
    # This is just a placeholder example
    return distance * 0.02  # Assuming 0.02 kg CO2 per mile

def calculate_bicycle_footprint(distance):
    # Example calculation for bicycle carbon footprint
    # You can replace this with your own calculation method
    # This is just a placeholder example
    return 0  # Assuming 0 kg CO2 for bicycle
# charging_locator/views.py


def community(request):
    # Sample list of stations with names, city names, and IDs
    stations = [
        {'id': 1, 'name': 'Station A', 'city': 'New York'},
        {'id': 2, 'name': 'Station B', 'city': 'Los Angeles'},
        {'id': 3, 'name': 'Station C', 'city': 'Chicago'},
    ]

    return render(request, 'charging_locator/community.html', {'stations': stations})

def charging_station_detail(request, station_id):
    charging_station = get_object_or_404(ChargingStation, pk=station_id)
    
    # Get existing reviews for the charging station
    reviews = ChargingStationReview.objects.filter(charging_station=charging_station)
    
    # Calculate average rating
    rating = ChargingStationRating.objects.filter(charging_station=charging_station).first()
    
    if request.method == 'POST':
        form = ChargingStationReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.charging_station = charging_station
            review.user = request.user  # Assuming user is authenticated
            review.save()
            
            # Update average rating
            if rating:
                rating.update_average_rating()
            else:
                ChargingStationRating.objects.create(charging_station=charging_station).update_average_rating()
            
            return redirect('charging_station_detail', station_id=station_id)
    else:
        form = ChargingStationReviewForm()
    
    return render(request, 'charging_locator/charging_station_detail.html', {'charging_station': charging_station, 'reviews': reviews, 'rating': rating, 'form': form})

def submit_charging_station_review(request, station_id):
    charging_station = get_object_or_404(ChargingStation, pk=station_id)
    
    if request.method == 'POST':
        form = ChargingStationReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.charging_station = charging_station
            review.user = request.user  # Assuming user is authenticated
            review.save()
            
            # Update average rating
            rating, created = ChargingStationRating.objects.get_or_create(charging_station=charging_station)
            rating.update_average_rating()
            
            return redirect('charging_station_detail', station_id=station_id)
    else:
        # If request method is not POST, redirect to charging station detail page
        return redirect('charging_station_detail', station_id=station_id)