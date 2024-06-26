class RobotActions:

    skiing_frames = [
        # starting position
        {
            "time": 400,
            "data": {
                "body.arms.right.upper.pitch": -0.5,
                "body.arms.left.upper.pitch": -0.5,
            },
        },
        # right ski push
        {
            "time": 1000,
            "data": {
                "body.arms.right.upper.pitch": -1.0,
                "body.arms.left.upper.pitch": 1.0,
            },
        },
        # left ski push
        {
            "time": 2000,
            "data": {
                "body.arms.right.upper.pitch": 1.0,
                "body.arms.left.upper.pitch": -1.0,
            },
        },
        # return to starting position
        {
            "time": 2400,
            "data": {
                "body.arms.right.upper.pitch": -0.5,
                "body.arms.left.upper.pitch": -0.5,
            },
        },
    ]

    def __init__(self, session):
        self.session = session

    def touched(self, frame):
        if (
            "body.head.front" in frame["data"]
            or "body.head.middle" in frame["data"]
            or "body.head.rear" in frame["data"]
        ):
            # yield call("rie.dialogue.say", text="Ouch! Please don't touch me!")
            print("touch")

    def skiing_motion(self, frames=skiing_frames):
        print("Yes")
        yield self.session.call("rom.actuator.motor.write", frames=frames, force=True)
