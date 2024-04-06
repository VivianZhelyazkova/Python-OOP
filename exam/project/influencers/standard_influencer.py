from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class StandardInfluencer(BaseInfluencer):
    PAYMENT_PERCENT = 0.45
    CAMPAIGN_MULTIPLIER = {
        "HighBudgetCampaign": 1.2,
        "LowBudgetCampaign": 0.9
    }

    def calculate_payment(self, campaign: BaseCampaign) -> float:
        return campaign.budget * StandardInfluencer.PAYMENT_PERCENT

    def reached_followers(self, campaign_type: str):
        result = self.followers * self.engagement_rate * StandardInfluencer.CAMPAIGN_MULTIPLIER[campaign_type]
        return int(result)
