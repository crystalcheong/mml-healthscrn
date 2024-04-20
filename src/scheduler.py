from transitions import Machine

class HealthCareScheduler(object):
    states = ['start', 'collecting_name', 'checking_age', 'selecting_time', 'confirmation', 'completed', 'invalid_input', 'underage']

    def __init__(self):
        self.machine = Machine(model=self, states=HealthCareScheduler.states, initial='start')

        self.machine.add_transition('start_conversation', 'start', 'collecting_name', conditions=['is_looking_for_vaccine'])
        self.machine.add_transition('input_name', 'collecting_name', 'checking_age')
        self.machine.add_transition('input_age', 'checking_age', 'selecting_time', conditions=['is_adult'])
        self.machine.add_transition('input_age', 'checking_age', 'underage', unless=['is_adult'])
        self.machine.add_transition('select_time', 'selecting_time', 'confirmation')
        self.machine.add_transition('confirm', 'confirmation', 'completed')

        self.machine.add_transition('invalid_input', '*', 'invalid_input')
        self.machine.add_transition('handle_invalid', 'invalid_input', 'start')

    def is_looking_for_vaccine(self, response):
        return response.lower() in ['yes', 'sure']

    def is_adult(self, age):
        return age >= 18