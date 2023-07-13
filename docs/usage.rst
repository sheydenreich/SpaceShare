.. _usage:

Usage
=====

Before you begin, you need to create a ``config.cfg`` file to suit your needs.
You can use the ``example_config.cfg`` file as a starting point.
Note that you will have to modify the smtp port to suit your E-Mail address.
For all major E-Mail providers, you can find the correct port on the internet.
For googlemail, it can be found `here <https://support.google.com/a/answer/176600?hl=en>`_.

.. note::
    If you are using googlemail or any other provider that requires two-factor authentification, the E-Mail package will run into problems.
    For googlemail, you can circumvent this by creating and using an `app password <https://support.google.com/accounts/answer/185833?hl=en>`_.

.. note::
    Please note that, while you can provide a password in the config file, it is not recommended.
    If you do not provide a password you will be prompted for one when you run the script.
    This is the recommended way of doing it, as it will not store your password in plain text.

