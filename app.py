from src.scheduler import HealthCareScheduler
from src.interface import SchedulerConsoleInterface

import sys
def main():
  # Create an instance of the scheduler
  scheduler = HealthCareScheduler()

  # Pass the scheduler instance to the interface
  interface = SchedulerConsoleInterface(scheduler)

  # Run the interface
  interface.run()


if __name__ == "__main__":
  main()
