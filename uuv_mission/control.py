class PDController:
    def __init__(self, kp, kd):
        self.kp = kp    # Proportional gain
        self.kd = kd    # Derivative gain
        self.previous_error = 0.0   # Assume e[−1] = 0

    def compute_control(self, reference, observation):
        error = reference - observation
        delta_error = (error - self.previous_error)
        # Since dt = 1, we can simplify the derivative term to just delta_error

        control_signal = self.kp * error + self.kd * delta_error
        self.previous_error = error
        return control_signal