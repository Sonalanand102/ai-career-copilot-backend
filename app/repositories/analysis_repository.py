from app.models.analysis import Analysis


class AnalysisRepository:

    def __init__(self, db):
        self.db = db

    def create(
        self,
        analysis: Analysis
    ):

        self.db.add(
            analysis
        )

        self.db.commit()

        self.db.refresh(
            analysis
        )

        return analysis