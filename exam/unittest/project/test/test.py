from project.social_media import SocialMedia
import unittest


class TestSocialMedia(unittest.TestCase):
    def setUp(self):
        self.sm = SocialMedia("Pesho", "Instagram", 100, "cars")

    def test_init(self):
        expected = ["Pesho", "Instagram", 100, "cars", []]
        actual = [self.sm._username, self.sm.platform, self.sm.followers, self.sm._content_type, self.sm._posts]
        self.assertEqual(expected, actual)

    def test_followers_setter_raises(self):
        with self.assertRaises(ValueError) as error:
            self.sm.followers = -1
        self.assertEqual(str(error.exception), "Followers cannot be negative.")

    def test_followers_setter(self):
        self.sm.followers = 3
        expected = 3
        actual = self.sm.followers
        self.assertEqual(expected, actual)

    def test_validate_platform_raises(self):
        allowed_platforms = ['Instagram', 'YouTube', 'Twitter']
        with self.assertRaises(ValueError) as error:
            self.sm.platform = "dhgd"
        self.assertEqual(str(error.exception), f"Platform should be one of {allowed_platforms}")

    def test_validate_platform(self):
        self.sm.platform = "YouTube"
        expected = "YouTube"
        actual = self.sm.platform
        self.assertEqual(expected, actual)

    def test_create_post(self):
        actual_return = self.sm.create_post("post_content")
        expected = [{'content': "post_content", 'likes': 0, 'comments': []}]
        actual = self.sm._posts
        self.assertEqual(expected, actual)
        expected_return = "New cars post created by Pesho on Instagram."
        self.assertEqual(expected_return, actual_return)

    def test_like_post_invalid(self):
        actual = self.sm.like_post(2)
        expected = "Invalid post index."
        self.assertEqual(expected, actual)

    def test_like_post_maximum_likes(self):
        self.sm.create_post("post_content")
        self.sm._posts[0]["likes"] = 10
        actual_return = self.sm.like_post(0)
        expected_return = f"Post has reached the maximum number of likes."
        self.assertEqual(expected_return, actual_return)

    def test_like_post(self):
        self.sm.create_post("post_content")
        actual_return = self.sm.like_post(0)
        expected_return = f"Post liked by Pesho."
        self.assertEqual(expected_return, actual_return)
        expected = [{'content': "post_content", 'likes': 1, 'comments': []}]
        actual = self.sm._posts
        self.assertEqual(actual, expected)

    def test_comment_post_short(self):
        self.sm.create_post("post_content")
        actual = self.sm.comment_on_post(0, "g")
        expected = "Comment should be more than 10 characters."
        self.assertEqual(expected, actual)

    def test_comment_post(self):
        self.sm.create_post("post_content")
        actual_return = self.sm.comment_on_post(0, "12345678910")
        expected_return = f"Comment added by Pesho on the post."
        self.assertEqual(expected_return, actual_return)
        expected = [{'content': "post_content", 'likes': 0, 'comments': [{'user': "Pesho", 'comment': "12345678910"}]}]
        actual = self.sm._posts
        self.assertEqual(expected, actual)
