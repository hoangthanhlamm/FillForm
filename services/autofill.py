import random
import time
import urllib.parse

import requests


class AutoFill:
    def __init__(self, config):
        self.base_url = config.get('base_url')
        self.questions = config.get('questions')

    def get_url(self):
        params = {}
        for question in self.questions:
            question_id = question['id']
            answers = question['answers']
            # multichoice = question.get('multichoice', False)
            multichoice = False
            n_answers = random.randint(1, 2) if multichoice else 1
            ans = []
            for idx in range(n_answers):
                r = random.random()
                threshold = 0
                for answer, ratio in answers.items():
                    if r <= threshold + ratio:
                        ans.append(answer)
                        break
                    else:
                        threshold += ratio

            params[question_id] = ','.join(ans)

            if question_id not in params:
                print(f'Warning: {question_id} - ratio invalid')

        # queries = [f'{key}={value}' for key, value in params.items()]
        queries = urllib.parse.urlencode(params)
        url = f'{self.base_url}?{queries}&pageHistory=0,1,2'
        return url

    def get_urls(self, n_responses=10):
        urls = []
        cnt = 0
        for idx in range(n_responses):
            url = self.get_url()

            cnt += 1
            print(cnt)
            print(url)

            urls.append(url)
            requests.get(url)
            time.sleep(1)

        return urls

    def fill_contact_us(self, answer):
        params = {}
        for question in self.questions:
            question_id = question['id']
            answer_field = question['answers']
            params[question_id] = answer.get(answer_field, '')

        queries = urllib.parse.urlencode(params)
        url = f'{self.base_url}?{queries}'
        print(url)
        requests.get(url)
        return url
