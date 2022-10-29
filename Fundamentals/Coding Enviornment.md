# Coding Enviornment
##
Because we aren't pyschopaths <sup>[*citation needed*]</sup>, we have several ways of configuring our enviornment to make our lives easier. 
*Warning: This is all theoretical as of writing, and nothing has been discussed in any depth with the entire team. Until further update, take this all as possible maybe best practices*

<h1> Tools </h1>

<h2>Essentials</h2>
<details>
<summary>
VSCode
</summary>
    our primary code editor
</details>
<details>
<summary>
Github Desktop
</summary>
</details>
<details>
<summary>
Phoenix Tuner
</summary>
</details>
<details>
<summary>
Driver Station
</summary>
</details>
<h1> Comments and Regions </h1>
For commenting, we use the extensions for VSCode Better Comments and Region Viewer (found in extensions.json) which allows for more descriptive comments, along with in-code dropdowns. Following the rationale for these additions, along with usage advice.
<h2>Better Comments</h2>
Better Comments is good and can do no wrong. Basically, it gives you comment flavors to make green walls less common. Here is a standard for Custom comments, with the settings file found at comments.json (please don't feel obligated to use the exact file, just be mindful of the standard): 
<br>
<ul>
    <li>Normal comment, "//", used for whatever</li>
    <li>Explaination comment, "//:", used for explaining code</li>
    <li>Question comment, "//?", used for expressing concern or curiosity for parts of code</li>
    <li> todo comment, "//TODO", does exactly what it sounds like, also gives a notification for easy tracking</li>
    <li> nvm ig comment, "////", Used for comments no longer valid beyond getting a look into the process of some code</li>
    <li>NO NO N O comment, "//!", like a question comment but more accurately expresses your constant need for attention</li>
    

</ul>
**See the file commentexample.png**



<h2>Region Viewer</h2>
Region viewer allows for C#-inspired regions, special comments that are basically dropdowns. The syntax goes like: <br>
`//#region my very own region

System.println("this isn't a comment, but actual code");

//#endregion my very own region

`
Note that the //#endregion doesn't need the name of the region, but it helps with organization and is encouraged