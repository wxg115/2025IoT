#include <LedToggle.h>
LedToggle led(LED_BUILTIN);
void setup() {
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:
  led.toggle();
  delay(500);
}
