from django.test import TestCase

from . import models

class O2OTestCase(TestCase):
    def test_delete_o2o_child(self):
        thing = models.Thing.objects.create(name='thing')

        with self.assertRaises(models.ThingAttachment.DoesNotExist):
            thing.attachment

        attachment = models.ThingAttachment.objects.create(name='attachment', thing=thing)

        self.assertEqual(thing.attachment, attachment)
        thing.attachment.delete()

        # I would expect thing.attachment to not exist, but apparently it does:
        # this test passes
        self.assertEqual(thing.attachment.name, 'attachment')

        # I thought maybe assigning None would be a good thing, but it doesn't work.
        with self.assertRaises(ValueError):
            thing.attachment = None

        # This is the best workaround I have
        thing = models.Thing.objects.get(pk=thing.pk)
        with self.assertRaises(models.ThingAttachment.DoesNotExist):
            thing.attachment
