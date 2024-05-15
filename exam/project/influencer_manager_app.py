from typing import List

from project.campaigns.base_campaign import BaseCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer



class InfluencerManagerApp:
    INFLUENCERS = {
        "PremiumInfluencer": PremiumInfluencer,
        "StandardInfluencer": StandardInfluencer,
    }
    CAMPAIGNS = {
        "HighBudgetCampaign": HighBudgetCampaign,
        "LowBudgetCampaign": LowBudgetCampaign
    }

    def __init__(self):
        self.influencers: List[BaseInfluencer] = []
        self.campaigns: List[BaseCampaign] = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in InfluencerManagerApp.INFLUENCERS:
            return f"{influencer_type} is not an allowed influencer type."
        searched_influencer = next((influencer for influencer in self.influencers if influencer.username == username),
                                   None)
        if searched_influencer:
            return f"{username} is already registered."
        influencer = InfluencerManagerApp.INFLUENCERS[influencer_type](username, followers, engagement_rate)
        self.influencers.append(influencer)
        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in InfluencerManagerApp.CAMPAIGNS:
            return f"{campaign_type} is not a valid campaign type."
        searched_campaign = next((campaign for campaign in self.campaigns if campaign_id == campaign.campaign_id), None)
        if searched_campaign:
            return f"Campaign ID {campaign_id} has already been created."
        campaign = InfluencerManagerApp.CAMPAIGNS[campaign_type](campaign_id, brand, required_engagement)
        self.campaigns.append(campaign)
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        influencer = next((influencer for influencer in self.influencers if influencer.username == influencer_username),
                          None)
        campaign = next((campaign for campaign in self.campaigns if campaign_id == campaign.campaign_id), None)
        if not influencer:
            return f"Influencer '{influencer_username}' not found."
        if not campaign:
            return f"Campaign with ID {campaign_id} not found."
        if not campaign.check_eligibility(influencer.engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."
        payment = influencer.calculate_payment(campaign)
        if payment < 0.0:
            return
        campaign.approved_influencers.append(influencer)
        campaign.budget -= payment
        influencer.campaigns_participated.append(campaign)
        return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self):
        result = {}
        for campaign in self.campaigns:
            if not campaign.approved_influencers:
                continue
            result[campaign] = sum([influencer.reached_followers(campaign.__class__.__name__) for influencer in campaign.approved_influencers])
        return result

    def influencer_campaign_report(self, username: str):
        influencer = next(influencer for influencer in self.influencers if influencer.username == username)
        return influencer.display_campaigns_participated()

    def campaign_statistics(self):
        sorted_campaigns = list(
            sorted(self.campaigns, key=lambda campaign: (len(campaign.approved_influencers), -campaign.budget)))
        result = "$$ Campaign Statistics $$"
        for campaign in sorted_campaigns:
            followers = sum([influencer.reached_followers(campaign.__class__.__name__) for influencer in campaign.approved_influencers])
            result += f"\n  * Brand: {campaign.brand}, Total influencers: {len(campaign.approved_influencers)}, Total budget: ${campaign.budget:.2f}, Total reached followers: {followers}"
        return result