
Django Preview
==============

Django preview allows you to mark models as preview-able. This allows a 
modified version of an object in the database to be displayed via a special 
preview URL without writing those changes back to the database.

A great example where this can be useful is in a blogging application, where
you may wish to check changes to an already published post on the site without
saving the changes for all to see.