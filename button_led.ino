// Add Arduino core header at top
#include <Arduino.h> // [🧠: TEACH] Required for all Arduino core functions like pinMode/digitalWrite

// Define pins using constants for easy configuration
const int BUTTON_PIN = 2;               // Digital pin for button
const int LED_PIN = 13;                 // Digital pin for LED
const unsigned long ON_DURATION = 3000; // 3 seconds in milliseconds

// State tracking variables
unsigned long ledStartTime = 0;
bool ledActive = false;
int previousButtonState = HIGH;

void setup()
{
    pinMode(LED_PIN, OUTPUT);          // Set LED as output
    pinMode(BUTTON_PIN, INPUT_PULLUP); // Enable internal pull-up resistor for button
}

void loop()
{
    int currentButtonState = digitalRead(BUTTON_PIN);

    // Detect button press (falling edge detection)
    if (previousButtonState == HIGH && currentButtonState == LOW)
    {
        ledStartTime = millis(); // Record start time
        ledActive = true;        // Activate LED timer
        digitalWrite(LED_PIN, HIGH);
    }
    previousButtonState = currentButtonState; // Update state tracker

    // Check timer expiration non-blockingly
    // If LED is on AND 3 seconds have passed since LED was turned on (millis() - ledStartTime >= 3000ms)
    if (ledActive && (millis() - ledStartTime >= ON_DURATION))
    {
        digitalWrite(LED_PIN, LOW);
        ledActive = false; // Deactivate timer
    }
}