base_delay_ms = 150
retry_attempt_number = 4

Calculate = base_delay_ms * (retry_attempt_number**2)
print(Calculate)