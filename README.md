# Vaccination Appointment Scheduler

## Overview

This Python application implements a conversation model using a Finite State Machine (FSM) to guide users through scheduling a vaccination appointment. It leverages the `transitions` library to manage states and transitions in response to user inputs.

## Design Choices

### States and Transitions

The conversation flow is modeled through various states that reflect the steps in scheduling a vaccination appointment:

- **Initiating**: The bot asks if the user wants to schedule an appointment.
- **Collecting Name**: Collects the user's name.
- **Checking Age**: Verifies if the user is above 18 years old.
- **Showing Slots**: Displays available appointment slots.
- **Confirming**: Confirms the appointment details.
- **Completed**: Ends the conversation after scheduling the appointment.
- **Error Handling**: Manages invalid inputs and prompts the user to re-enter data.

Transitions between these states are triggered by user responses, ensuring the conversation progresses logically and intuitively:

- Transition from `initiating` to `collecting_name` occurs if the user affirms their intent to schedule.
- Errors or unclear inputs trigger a move to `error_handling`, which guides the user back into the flow.

### Methods for State Handling

Each state has associated methods that handle entering and exiting states, processing inputs, and transitioning to the next appropriate state. These methods ensure the conversation remains responsive and contextually relevant.

## Assumptions and Simplifications

- **User Inputs**: It is assumed that inputs are provided through a simulated interface or direct method calls within a controlled environment (e.g., testing frameworks).
- **Age Verification**: Simplistically assumes that any input above 18 qualifies without further verification.
- **Appointment Slots**: Available slots are pre-defined and static, presented as a list without real-time updating based on actual availability.

## Running the Application

To run this application, ensure you have Python and the `transitions` library installed. Execute the `scheduler.py` script through a Python interpreter. The `interface.py` script handles the interaction with users, simulating a conversation interface.

```bash
python app.py
```
