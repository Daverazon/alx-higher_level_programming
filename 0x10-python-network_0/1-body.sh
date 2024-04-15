#!/bin/bash
# It takes in a URL, sends a GET request to the URL, and displays the body of the response. -L option follows redirects till the final page.
curl -sL "$1"
