# Dionysia CTL
Small command line utility that allows me to fetch my next calendar entries
in that app we use for organizing our trainings.

For this to work you'll need two environment variables:

	export DIONYSIA_TOKEN=...
	export DIONYSIA_API_URL=https://.../api/student

DIONYSIA_TOKEN being a JWT token that you can obtain from /api/student/login
(normally they last for a month or so) and the API URL you can find out by
inspecting the phone App (you know which one).


