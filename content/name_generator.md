
  <h1>Voltine Name Generator</h1>
  <p>Click the button to generate your Voltine band name!</p>
  <button onclick="generateVoltineName()">Generate Name</button>

  <div id="thinking">
    Thinking<span class="dots"></span><span class="dots"></span><span class="dots"></span>
  </div>

  <div id="result"></div>

  <script>
    function generateVoltineName() {
      const electricalTerms = [
        "Amp", "Watt", "Ohm", "Volt", "Current", "Static", 
        "Surge", "Circuit", "Charge", "Spark", "Fuse", 
        "Resistor", "Conductor", "Capacitor", "Inductor", "Electric", 
        "Magnet", "Power", "Lightning", "Edison", "Tesla"
      ];

      const adjectives = [
        "Shocking", "Electrifying", "Charged", "Static", "High Voltage",
        "Wired", "Bright", "Buzzing", "Magnetic", "Overloaded", 
        "Supercharged", "Hot", "Flashing", "Live", "Sizzling"
      ];

      function getRandomElement(array) {
        return array[Math.floor(Math.random() * array.length)];
      }

      const thinkingDiv = document.getElementById("thinking");
      const resultDiv = document.getElementById("result");

      // Show thinking animation
      thinkingDiv.style.display = "block";
      resultDiv.innerText = "";

      // Simulate delay
      setTimeout(() => {
        const part1 = getRandomElement(adjectives);
        const part2 = getRandomElement(electricalTerms);

        const voltineName = `${part1} ${part2}`;

        // Hide thinking animation and display result
        thinkingDiv.style.display = "none";
        resultDiv.innerText = `Your Voltine name is: ${voltineName}`;
      }, 3000); // 3-second delay
    }
  </script>