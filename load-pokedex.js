const nationalDexPokemon = JSON.parse(nationalPokedex);
const normalDexPokemon = JSON.parse(normalDex);
const shinyDexPokemon = JSON.parse(shinyDex);

var pokemon = nationalDexPokemon.pokemon;
var pokedex = normalDexPokemon.pokemon;
var shinydex = shinyDexPokemon.pokemon;

function loadPokedex() {
    var pokedexContainer = document.getElementById("pokedex-cards-container");
    for (var i=0; i < pokemon.length; i++) {
        var dexEntry = pokedex[pokemon[i].Number - 1];
        //create card for each pokemon
        var pokemonCard = document.createElement("div");
        pokemonCard.className = "mdl-card mdl-shadow--3dp";
        //create title for each pokemon
        var pokemoneNameContainer = document.createElement("div");
        pokemoneNameContainer.className = "mdl-card__title mdl-card--border";
        var pokemoneName = document.createElement("h4");    
        pokemoneName.innerHTML = pokemon[i].Name + " (" + pokemon[i].Number + ")";
        pokemoneNameContainer.appendChild(pokemoneName);
        pokemonCard.appendChild(pokemoneNameContainer);
        //create image for each pokemon
        var pokemonNormalSpriteContainer = document.createElement("div");
        pokemonNormalSpriteContainer.className = "mdl-card__media mdl-card--border";
        var pokemonNormalSpriteContainerOverlay = document.createElement("div");
            if ((Object.values(dexEntry)) != "true") {
                pokemonNormalSpriteContainerOverlay.className = "missing";
            }
        var pokemonNormalSprite = document.createElement("img");
        pokemonNormalSprite.src = pokemon[i].NormalSprite;
        pokemonNormalSpriteContainerOverlay.appendChild(pokemonNormalSprite);
        pokemonNormalSpriteContainer.appendChild(pokemonNormalSpriteContainerOverlay);
        pokemonCard.appendChild(pokemonNormalSpriteContainer);

        //create tags for games each pokemon is in
        //var pokemonTextContainer = document.createElement("div");
        //pokemonTextContainer.className = "mdl-card__supporting-text mdl-card--border";
        //pokemonCard.appendChild(pokemonTextContainer);
        
        pokedexContainer.appendChild(pokemonCard);
    }
}

function shinyToggle(){
    console.log("shinyToggle");
    var toggle = document.getElementById("switch-2");
    if (toggle.checked == true){ 
        var pokedexContainer = document.getElementById("pokedex-cards-container");
        pokedexContainer.innerHTML = "";
        for (var i=0; i < pokemon.length; i++) {
            var shinyDexEntry = shinydex[pokemon[i].Number - 1];
            //create card for each pokemon
            var pokemonCard = document.createElement("div");
            pokemonCard.className = "mdl-card mdl-shadow--3dp";
            //create title for each pokemon
            var pokemoneNameContainer = document.createElement("div");
            pokemoneNameContainer.className = "mdl-card__title mdl-card--border";
            var pokemoneName = document.createElement("h4");    
            pokemoneName.innerHTML = pokemon[i].Name + " (" + pokemon[i].Number + ")";
            pokemoneNameContainer.appendChild(pokemoneName);
            pokemonCard.appendChild(pokemoneNameContainer);
            //create image for each pokemon
            var pokemonShinySpriteContainer = document.createElement("div");
            pokemonShinySpriteContainer.className = "mdl-card__media mdl-card--border";
            var pokemonShinySpriteContainerOverlay = document.createElement("div");
            if ((Object.values(shinyDexEntry)) != "true") {
                pokemonShinySpriteContainerOverlay.className = "missing";
            }
            var pokemonShinySprite = document.createElement("img");
            pokemonShinySprite.src = pokemon[i].ShinySprite;
            pokemonShinySpriteContainerOverlay.appendChild(pokemonShinySprite);
            pokemonShinySpriteContainer.appendChild(pokemonShinySpriteContainerOverlay);
            pokemonCard.appendChild(pokemonShinySpriteContainer);

            //create tags for games each pokemon is in
            var pokemonTextContainer = document.createElement("div");
            pokemonTextContainer.className = "mdl-card__supporting-text mdl-card--border";
            var pokemonText = document.createElement("p");
            pokemonText.innerHTML = Object.values(shinyDexEntry);
            pokemonTextContainer.appendChild(pokemonText);
            pokemonCard.appendChild(pokemonTextContainer);

            pokedexContainer.appendChild(pokemonCard);
        }
    } else { 
        var pokedexContainer = document.getElementById("pokedex-cards-container");
        pokedexContainer.innerHTML = "";
        for (var i=0; i < pokemon.length; i++) {
            var dexEntry = pokedex[pokemon[i].Number - 1];
        //create card for each pokemon
        var pokemonCard = document.createElement("div");
        pokemonCard.className = "mdl-card mdl-shadow--3dp";
        //create title for each pokemon
        var pokemoneNameContainer = document.createElement("div");
        pokemoneNameContainer.className = "mdl-card__title mdl-card--border";
        var pokemoneName = document.createElement("h4");    
        pokemoneName.innerHTML = pokemon[i].Name + " (" + pokemon[i].Number + ")";
        pokemoneNameContainer.appendChild(pokemoneName);
        pokemonCard.appendChild(pokemoneNameContainer);
        //create image for each pokemon
        var pokemonNormalSpriteContainer = document.createElement("div");
        pokemonNormalSpriteContainer.className = "mdl-card__media mdl-card--border";
        var pokemonNormalSpriteContainerOverlay = document.createElement("div");
            if ((Object.values(dexEntry)) != "true") {
                pokemonNormalSpriteContainerOverlay.className = "missing";
            }
        var pokemonNormalSprite = document.createElement("img");
        pokemonNormalSprite.src = pokemon[i].NormalSprite;
        pokemonNormalSpriteContainerOverlay.appendChild(pokemonNormalSprite);
        pokemonNormalSpriteContainer.appendChild(pokemonNormalSpriteContainerOverlay);
        pokemonCard.appendChild(pokemonNormalSpriteContainer);

        //create tags for games each pokemon is in
        //var pokemonTextContainer = document.createElement("div");
        //pokemonTextContainer.className = "mdl-card__supporting-text mdl-card--border";
        //pokemonCard.appendChild(pokemonTextContainer);
        
        pokedexContainer.appendChild(pokemonCard);
        }
    }
}

window.onload = loadPokedex;
