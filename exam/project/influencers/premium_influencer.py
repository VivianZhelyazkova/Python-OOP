from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class PremiumInfluencer(BaseInfluencer):
    PAYMENT_PERCENT = 0.85
    CAMPAIGN_MULTIPLIER = {
        "HighBudgetCampaign": 1.5,
        "LowBudgetCampaign": 0.8
    }

    def calculate_payment(self, campaign: BaseCampaign) -> float:
        return campaign.budget * PremiumInfluencer.PAYMENT_PERCENT

    def reached_followers(self, campaign_type: str):
        result = self.followers * self.engagement_rate * PremiumInfluencer.CAMPAIGN_MULTIPLIER[campaign_type]
        return int(result)
