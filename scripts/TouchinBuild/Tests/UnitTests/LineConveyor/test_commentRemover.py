import unittest
from Core.LineConveyor.CommentRemover import CommentRemover


class TestCommentRemover(unittest.TestCase):
	def setUp(self):
		self.commentRemover = CommentRemover()

	def test_startsWithComment(self):
		line = '# this line is comment'
		newLine = self.commentRemover.processText(line)

		self.assertEqual('', newLine)

	def test_containsComment(self):
		line = 'this line contains # a comment'
		newLine = self.commentRemover.processText(line)

		self.assertEqual('this line contains ', newLine)