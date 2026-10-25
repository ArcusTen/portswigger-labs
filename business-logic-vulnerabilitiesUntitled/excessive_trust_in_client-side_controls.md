
![[Pasted image 20261025202427.png]]

instance: `https://0a8f00af0408a07b810f0ccc0068009e.web-security-academy.net/`

Open it in burpsuite proxy:

![[Pasted image 20261025201156.png]]

Login as `wiener:peter` as prescribed by lab description, we have store credit **100$**:

![[Pasted image 20261025201246.png]]

So our goal for this lab is to and  exploit a logic flaw in its purchasing workflow to buy items for an unintended price buy Lightweight l33t leather jacket. Price of this jacket is **1337$**, clearly out of our budget:

![[Pasted image 20261025201452.png]]

Click on view details, scroll down and click on add to cart while interceptor enabled in burpsuite:

![[Pasted image 20261025201540.png]]

![[Pasted image 20261025201603.png]]

A post request is captured in burpsuite:

![[Pasted image 20261025201640.png]]

Here, we can see that added item request contains a `price` parameter. 

When analyzing multi-step processes, such as order completion or privilege modification, we identify the HTTP request parameters and confirmation endpoints responsible for controlling the application’s state.

If the backend does not properly validate prerequisites on the server side, an attacker may manipulate request parameters or directly access confirmation endpoints to perform unauthorized actions.

By modifying the request in Burp Suite Repeater to execute the final step directly, we demonstrated that the application could process the action without verifying whether the preceding steps had been completed. This successfully fulfilled the lab requirement and highlighted a weakness in the application's server-side state validation.

We are going to change the price to an some small value and send the request. 

![[Pasted image 20261025201822.png]]

We got a `302` response.

Now, lets refresh the cart and confirm that the price or not. Price is showing 1337 but we are not seeing any insufficient credits message, lets try to place the order:

![[Pasted image 20261025202213.png]]

We have solved the lab:

![[Pasted image 20261025202103.png]]