
![[Pasted image 20261025202548.png]]

instance: `https://0a82005604a7715a8209b56200bf0009.web-security-academy.net/`

Now for this lab, we have an an admin panel at `/admin`, we have to modify cookie to become admin and delete user carlos to solve this lab.


Login as provided user `wiener:peter`:

![[Pasted image 20261025203111.png]]

Lets try to visit `/admin` endpoint:

![[Pasted image 20261025203138.png]]

We aren't admin right now. Lets see cookie section in browser's developer tools (ctrl+shift+I):

![[Pasted image 20261025203317.png]]

Change that value to `true` and refresh page:

![[Pasted image 20261025203404.png]]

As you can see we are admin now, as we can see delete wiener option. Lets complete the lab by deleting user carlos. Poor carlos :(

![[Pasted image 20261025203455.png]]