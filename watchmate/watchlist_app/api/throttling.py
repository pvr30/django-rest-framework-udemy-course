from rest_framework.throttling import UserRateThrottle


class ReviewListThrottle(UserRateThrottle):
    scope = 'review-list'


class ReviewCreateThrottle(UserRateThrottle):
    scope = 'review-create'
