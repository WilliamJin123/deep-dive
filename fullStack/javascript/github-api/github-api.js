
const search_btn = document.getElementById("search-button");
const user_input = document.getElementById("username-input");
const user_info = document.getElementById("user-info");
const profile = document.getElementById("profile-display");

search_btn.onclick = async () => {  
    const username = user_input.value.trim();

    try {
        profile.innerHTML = ``
        if (username == "") {
            console.log('empty')
            throw new Error("Username cannot be empty")
        }
        const response = await fetch(`https://api.github.com/users/${username}`)
        const result = await response.json();
        if (!response.ok) {
            console.error('not ok')
            console.error(result)
            throw new Error(result.message || "User not found")
        }
        
        const avatar = document.createElement("img")
        avatar.src = result.avatar_url
        avatar.alt = `${result.login} avatar`
        avatar.style.width = '100px';
        avatar.style.height = '100px';
        avatar.style.borderRadius = '50%';
        profile.appendChild(avatar);

        const name = document.createElement('h2');
        name.textContent = result.name || result.login;
        profile.appendChild(name);

        const bio = document.createElement('p');
        bio.textContent = result.bio || 'No bio available.';
        profile.appendChild(bio);


    } catch (err) {
        const errorSection = user_info.querySelector("#error-message-container")
        const error = document.createElement("div")
        error.innerText = err.message
        error.classList.add("error")
        errorSection.appendChild(error)
        setTimeout(() => {
            error.classList.add("fade-out")
            setTimeout(() => {
                error.remove()
            }, 500)
        }, 4500)
    }
}