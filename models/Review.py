class Review():
    def __init__(self) -> None:
        self._critic_score = 0
        self._viewer_score = 0
        self._avg_review_score = 0

    # Setter Getters
    @property
    def critic_score(self)->int:
        return self._critic_score
    @critic_score.setter
    def critic_score(self, value)->None:
        self._critic_score = value

    @property
    def viewer_score(self)->int:
        return self._viewer_score
    @viewer_score.setter
    def viewer_score(self, value)->None:
        self._viewer_score = value

    @property
    def avg_review_score(self)->float:
        return self._avg_review_score
    @avg_review_score.setter
    def avg_review_score(self, value)->None:
        self._avg_review_score = value
    # Setter Getters end

    # Dunders for CLI
    def __str__(self):
        return "\tViewer Score: " + str(self.viewer_score) + "\n\tCritic Score: " + str(self.critic_score) + "\n\tAverage Review Score: " + str(self.avg_review_score)
    def __repr__(self):
        return "\tViewer Score: " + str(self.viewer_score) + "\n\tCritic Score: " + str(self.critic_score) + "\n\tAverage Review Score: " + str(self.avg_review_score)

    def update_critic_score(self, score:int, factor:int) -> None:
        self._critic_score += (score * factor)

    def update_viewer_score(self, score:int) -> None:
        self._viewer_score += score

    def get_total_score(self)->float:
        return self._critic_score + self._viewer_score