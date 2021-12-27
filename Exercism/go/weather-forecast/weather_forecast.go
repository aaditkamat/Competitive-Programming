// Package weather allows users to generate the weather forecast.
package weather

// CurrentCondition is used to store the condition at the current time.
var CurrentCondition string
// CurrentLocation is used to store the location provided at the current time.
var CurrentLocation string

/*
Forecast returns a string that represent the weather forecast based on the supplied
parameters for city and condition.
*/
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
