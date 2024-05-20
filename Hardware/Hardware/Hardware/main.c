#define F_CPU 16000000UL  // Define CPU frequency for delay functions (example: 16 MHz)
#include <avr/io.h>
#include <util/delay.h>

// Define pin connections
#define RS_PIN   PD0
#define EN_PIN   PD1
#define D4_PIN   PB2
#define D5_PIN   PB3
#define D6_PIN   PB4
#define D7_PIN   PB5

// Function to send command to LCD
void lcd_command(unsigned char command) {
	// Set RS pin LOW for command mode
	PORTD &= ~(1 << RS_PIN);

	// Set EN pin HIGH
	PORTD |= (1 << EN_PIN);

	// Send higher nibble
	PORTB = (PORTB & 0x0F) | (command & 0xF0);
	// Pulse EN pin
	PORTD &= ~(1 << EN_PIN);
	_delay_us(1);

	// Send lower nibble
	PORTB = (PORTB & 0x0F) | ((command & 0x0F) << 4);
	// Pulse EN pin
	PORTD &= ~(1 << EN_PIN);
	_delay_us(100);
}

// Function to send data to LCD
void lcd_data(unsigned char data) {
	// Set RS pin HIGH for data mode
	PORTD |= (1 << RS_PIN);

	// Set EN pin HIGH
	PORTD |= (1 << EN_PIN);

	// Send higher nibble
	PORTB = (PORTB & 0x0F) | (data & 0xF0);
	// Pulse EN pin
	PORTD &= ~(1 << EN_PIN);
	_delay_us(1);

	// Send lower nibble
	PORTB = (PORTB & 0x0F) | ((data & 0x0F) << 4);
	// Pulse EN pin
	PORTD &= ~(1 << EN_PIN);
	_delay_us(100);
}

// Function to initialize LCD
// Function to initialize LCD
void lcd_init() {
	// Set data direction for LCD pins
	DDRB |= 0xF0;  // D4-D7
	DDRD |= (1 << RS_PIN) | (1 << EN_PIN);  // RS, EN

	// Initial commands for LCD initialization
	_delay_ms(50);
	lcd_command(0x33);  // Initialize
	lcd_command(0x32);  // Set to 4-bit mode
	lcd_command(0x28);  // 2 lines, 5x8 font
	lcd_command(0x0C);  // Display on, cursor off, blinking off
	lcd_command(0x06);  // Increment cursor
	lcd_command(0x01);  // Clear display
	_delay_ms(10);      // Increase delay after clear display command
}


// Function to print a string on LCD
void lcd_print(const char* str) {
	while (*str) {
		lcd_data(*str++);
	}
}

int main() {
	// Initialize LCD
	lcd_init();

	// Display message
	lcd_command(0x80);  // Set cursor to line 1
	lcd_print("Hello, World!");
	_delay_ms(1000);     // Delay after printing message

	while (1) {
		// Your main code here
	}

	return 0;
}
