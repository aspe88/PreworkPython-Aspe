SELECT * FROM flights
WHERE status = 'On Time'

SELECT * FROM bookings
WHERE total_amount > 1000000

SELECT * FROM aircrafts_data

SELECT flight_id FROM flights
WHERE aircraft_code = '733'

SELECT * FROM tickets
Where passenger_name LIKE 'IRINA%'