import requests
import json
import pandas as pd



class GraphAPI:
    def __init__(self, fb_api):
        self.base_url = "https://graph.facebook.com/v14.0/" 
        self.api_fields = ["spend", "cpc", "cpm", "objective", "adset_name",
               "adset_id", "clicks", "capaign_name", "capaign_id",
               "conversions", "frequency", "conversion_values", "ad_names", "ad_id"]
        self.token = "&acess_token" + fb_api

    def get_insights(self, ad_acc, level="campaign"):
        url = self.base_url + "act_" + str(ad_acc)


if __name__ == "__main__":
    fb_api = open("lastdance/fb_token").read()
    ad_acc = "3120164588217844"

    self = GraphAPI(ad_acc, fb_api)