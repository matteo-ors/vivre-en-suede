require('dotenv').config();
const OpenAI = require('openai');
const fs = require('fs');
const path = require('path');
const https = require('https');

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });
const IMAGES_DIR = path.join(__dirname, 'images');
const STYLE = 'Professional travel photography, high quality, natural lighting, vibrant colors, no text, no watermarks, no logos.';

// ============================================================
// ALL MISSING SWEDISH IMAGES
// ============================================================

const images = [

  // ─── CITY OVERVIEW CARDS (800x600 equivalent → 1024x1024) ─────
  { filename: 'city-stockholm.jpg', prompt: `Aerial view of Stockholm, Sweden, Gamla Stan old town with colorful buildings, water surrounding the islands, blue sky summer day. ${STYLE}` },
  { filename: 'city-goteborg.jpg', prompt: `View of Göteborg, Sweden waterfront with canal boats, Haga district colorful buildings, Swedish west coast city. ${STYLE}` },
  { filename: 'city-malmo.jpg', prompt: `Malmö, Sweden skyline with Turning Torso tower, Öresund bridge in distance, modern waterfront, sunny day. ${STYLE}` },
  { filename: 'city-uppsala.jpg', prompt: `Uppsala, Sweden with the grand Uppsala Cathedral (Uppsala domkyrka), university buildings, Fyris river, autumn trees. ${STYLE}` },
  { filename: 'city-linkoping.jpg', prompt: `Linköping, Sweden city center with Linköping Cathedral, charming streets, Stångån river, typical Swedish architecture. ${STYLE}` },
  { filename: 'city-vasteras.jpg', prompt: `Västerås, Sweden lakefront view on Lake Mälaren, cathedral visible, Swedish small city charm, summer. ${STYLE}` },
  { filename: 'city-orebro.jpg', prompt: `Örebro, Sweden with the famous Örebro Castle reflected in Svartån river, park surroundings, blue sky. ${STYLE}` },
  { filename: 'city-norrkoping.jpg', prompt: `Norrköping, Sweden industrial landscape district with red brick buildings along Motala ström rapids, unique Swedish city. ${STYLE}` },
  { filename: 'city-helsingborg.jpg', prompt: `Helsingborg, Sweden with Kärnan medieval tower, harbor view towards Denmark, colorful buildings along the coast. ${STYLE}` },
  { filename: 'city-jonkoping.jpg', prompt: `Jönköping, Sweden lakefront on Lake Vättern, city skyline, matches museum area, peaceful Swedish lake city. ${STYLE}` },
  { filename: 'city-umea.jpg', prompt: `Umeå, Sweden in winter with birch trees, university campus area, northern Swedish city, snow and northern lights sky. ${STYLE}` },
  { filename: 'city-lund.jpg', prompt: `Lund, Sweden with Lund Cathedral (Lunds domkyrka), cobblestone streets, university town atmosphere, autumn. ${STYLE}` },
  { filename: 'city-gavle.jpg', prompt: `Gävle, Sweden city center with historic wooden buildings, Gavleån river, typical Swedish coastal town. ${STYLE}` },
  { filename: 'city-boras.jpg', prompt: `Borås, Sweden city center with textile heritage, modern street art, Viskan river, Swedish west coast inland city. ${STYLE}` },
  { filename: 'city-eskilstuna.jpg', prompt: `Eskilstuna, Sweden with Eskilstuna river (Eskilstunaån), industrial heritage buildings, parks, Swedish Mälardalen region. ${STYLE}` },
  { filename: 'city-sundsvall.jpg', prompt: `Sundsvall, Sweden stone city center rebuilt after the 1888 fire, Norrland architecture, northern Swedish coast. ${STYLE}` },
  { filename: 'city-karlstad.jpg', prompt: `Karlstad, Sweden on Klarälven river delta at Lake Vänern, sun sculpture, charming Swedish city. ${STYLE}` },
  { filename: 'city-vaxjo.jpg', prompt: `Växjö, Sweden with lake Växjösjön, cathedral, green sustainable city in Småland region. ${STYLE}` },
  { filename: 'city-halmstad.jpg', prompt: `Halmstad, Sweden coastal city, Nissan river, castle, sandy beaches, Swedish Halland coast summer. ${STYLE}` },

  // ─── CITY HERO IMAGES (panoramic) ────────────────────────────
  { filename: 'stockholm-hero.jpg', size: '1792x1024', prompt: `Breathtaking panoramic view of Stockholm, Sweden at golden hour, Gamla Stan old town, Riddarholmen church, water reflections, islands and bridges, stunning Swedish capital skyline. ${STYLE}` },
  { filename: 'goteborg-hero.jpg', size: '1792x1024', prompt: `Wide panoramic view of Göteborg, Sweden harbor and canals, Gothenburg Opera House, Älvsborgsbron bridge in distance, boats, Swedish west coast atmosphere. ${STYLE}` },
  { filename: 'malmo-hero.jpg', size: '1792x1024', prompt: `Panoramic view of Malmö, Sweden with Turning Torso, Västra Hamnen waterfront, Öresund bridge in background, modern and historic mix, sunny. ${STYLE}` },
  { filename: 'uppsala-hero.jpg', size: '1792x1024', prompt: `Panoramic view of Uppsala, Sweden from above, dominating Uppsala Cathedral, Uppsala Castle, Fyris river running through city, university gardens. ${STYLE}` },
  { filename: 'linkoping-hero.jpg', size: '1792x1024', prompt: `Panoramic view of Linköping, Sweden with cathedral, Stångån river, mix of historic and modern buildings, green Swedish city. ${STYLE}` },
  { filename: 'vasteras-hero.jpg', size: '1792x1024', prompt: `Panoramic view of Västerås, Sweden from Lake Mälaren side, cathedral skyline, waterfront promenade, Swedish Mälardalen. ${STYLE}` },
  { filename: 'orebro-hero.jpg', size: '1792x1024', prompt: `Panoramic view of Örebro, Sweden with Örebro Castle prominently in center, Svartån river, city park, wide angle. ${STYLE}` },
  { filename: 'norrkoping-hero.jpg', size: '1792x1024', prompt: `Panoramic view of Norrköping, Sweden industrial landscape with red brick factories along Motala ström rapids, waterfalls in city center. ${STYLE}` },
  { filename: 'helsingborg-hero.jpg', size: '1792x1024', prompt: `Panoramic view of Helsingborg, Sweden from harbor, Kärnan tower on hill, city terraces, view across Öresund to Denmark. ${STYLE}` },
  { filename: 'jonkoping-hero.jpg', size: '1792x1024', prompt: `Panoramic view of Jönköping, Sweden at Lake Vättern shore, city center, Munksjön lake, surrounded by Småland forests. ${STYLE}` },
  { filename: 'umea-hero.jpg', size: '1792x1024', prompt: `Panoramic view of Umeå, Sweden, birch-lined avenues, Umeälven river, university campus, northern Swedish winter light, snow. ${STYLE}` },
  { filename: 'lund-hero.jpg', size: '1792x1024', prompt: `Panoramic view of Lund, Sweden historic university town, Lund Cathedral dominating skyline, cobblestone streets, academic atmosphere. ${STYLE}` },
  { filename: 'gavle-hero.jpg', size: '1792x1024', prompt: `Panoramic view of Gävle, Sweden with Gavleån river, historic wooden houses, coastal Norrland town, Swedish east coast. ${STYLE}` },
  { filename: 'boras-hero.jpg', size: '1792x1024', prompt: `Panoramic view of Borås, Sweden with Viskan river, textile district heritage, modern street art murals on buildings. ${STYLE}` },
  { filename: 'eskilstuna-hero.jpg', size: '1792x1024', prompt: `Panoramic view of Eskilstuna, Sweden with Eskilstunaån river, industrial heritage, green parks, Swedish Sörmland region. ${STYLE}` },
  { filename: 'sundsvall-hero.jpg', size: '1792x1024', prompt: `Panoramic view of Sundsvall, Sweden stone city, northern Norrland coast, Södra and Norra berget mountains framing the city. ${STYLE}` },
  { filename: 'karlstad-hero.jpg', size: '1792x1024', prompt: `Panoramic view of Karlstad, Sweden at Klarälven river delta, Lake Vänern in distance, sun city of Sweden, bridges. ${STYLE}` },
  { filename: 'vaxjo-hero.jpg', size: '1792x1024', prompt: `Panoramic view of Växjö, Sweden, green city surrounded by lakes and Småland forests, cathedral, sustainable architecture. ${STYLE}` },
  { filename: 'halmstad-hero.jpg', size: '1792x1024', prompt: `Panoramic view of Halmstad, Sweden, Nissan river meeting the sea, Halmstad Castle, sandy beaches of Halland coast. ${STYLE}` },

  // ─── STOCKHOLM NEIGHBORHOODS ─────────────────────────────────
  { filename: 'stockholm-sodermalm.jpg', prompt: `Södermalm neighborhood in Stockholm, Sweden, trendy cafes, vintage shops, colorful buildings, hipster district, street life. ${STYLE}` },
  { filename: 'stockholm-ostermalm.jpg', prompt: `Östermalm neighborhood in Stockholm, Sweden, elegant boulevards, luxury shops, Strandvägen waterfront, upscale Swedish living. ${STYLE}` },
  { filename: 'stockholm-vasastan.jpg', prompt: `Vasastan neighborhood in Stockholm, Sweden, charming residential streets, Odenplan area, Stockholm Observatory park, cozy. ${STYLE}` },
  { filename: 'stockholm-kungsholmen.jpg', prompt: `Kungsholmen island in Stockholm, Sweden, waterfront walks, Stockholm City Hall (Stadshuset), residential calm, parks. ${STYLE}` },
  { filename: 'stockholm-hammarby.jpg', prompt: `Hammarby Sjöstad in Stockholm, Sweden, modern eco-district, waterfront apartments, sustainable urban living, canal. ${STYLE}` },
  { filename: 'stockholm-gamlastan.jpg', prompt: `Gamla Stan old town in Stockholm, Sweden, narrow medieval cobblestone streets, colorful 17th century buildings, Royal Palace nearby. ${STYLE}` },

  // ─── GÖTEBORG NEIGHBORHOODS ──────────────────────────────────
  { filename: 'goteborg-haga.jpg', prompt: `Haga district in Göteborg, Sweden, charming wooden houses (landshövdingehus), cozy cafes, cobblestone street, fika culture. ${STYLE}` },
  { filename: 'goteborg-centrum.jpg', prompt: `Göteborg city center, Sweden, Kungsportsavenyn boulevard, trams, shopping, lively Swedish west coast urban life. ${STYLE}` },
  { filename: 'goteborg-linne.jpg', prompt: `Linnéstaden in Göteborg, Sweden, trendy restaurants, Linnégatan street, bohemian atmosphere, residential charm. ${STYLE}` },
  { filename: 'goteborg-majorna.jpg', prompt: `Majorna neighborhood in Göteborg, Sweden, working-class heritage, local markets, community feeling, colorful facades. ${STYLE}` },
  { filename: 'goteborg-langedrag.jpg', prompt: `Långedrag in Göteborg, Sweden, seaside neighborhood, sailboats, archipelago views, peaceful Swedish coastal living. ${STYLE}` },
  { filename: 'goteborg-orgryte.jpg', prompt: `Örgryte neighborhood in Göteborg, Sweden, green residential area, villas, family-friendly, near Liseberg park. ${STYLE}` },

  // ─── MALMÖ NEIGHBORHOODS ─────────────────────────────────────
  { filename: 'malmo-vastrahamnen.jpg', prompt: `Västra Hamnen in Malmö, Sweden, modern waterfront with Turning Torso, sustainable architecture, seaside promenade, sunset. ${STYLE}` },
  { filename: 'malmo-davidshall.jpg', prompt: `Davidshall neighborhood in Malmö, Sweden, trendy area with cafes and boutiques, Art Nouveau buildings, urban charm. ${STYLE}` },
  { filename: 'malmo-mollevangen.jpg', prompt: `Möllevången in Malmö, Sweden, multicultural neighborhood, lively market square, diverse food scene, vibrant. ${STYLE}` },
  { filename: 'malmo-limhamn.jpg', prompt: `Limhamn in Malmö, Sweden, seaside village feel, limestone quarry lake, marina, family residential area. ${STYLE}` },
  { filename: 'malmo-ribersborg.jpg', prompt: `Ribersborg in Malmö, Sweden, Ribersborg beach (Ribban), Kallbadhuset bathhouse, Öresund views, summer. ${STYLE}` },
  { filename: 'malmo-gamlastad.jpg', prompt: `Gamla Staden old town in Malmö, Sweden, Stortorget square, half-timbered buildings, historic center, Malmöhus Castle nearby. ${STYLE}` },

  // ─── UPPSALA NEIGHBORHOODS ───────────────────────────────────
  { filename: 'uppsala-centrum.jpg', prompt: `Uppsala city center, Sweden, pedestrian shopping streets, cathedral in background, student life, bikes everywhere. ${STYLE}` },
  { filename: 'uppsala-luthagen.jpg', prompt: `Luthagen neighborhood in Uppsala, Sweden, residential area near university, charming houses, leafy streets, academic atmosphere. ${STYLE}` },
  { filename: 'uppsala-svartbacken.jpg', prompt: `Svartbäcken neighborhood in Uppsala, Sweden, student area, Ekonomikum nearby, affordable living, bikes. ${STYLE}` },
  { filename: 'uppsala-eriksberg.jpg', prompt: `Eriksberg in Uppsala, Sweden, modern residential area, families, parks, new construction, suburban Swedish living. ${STYLE}` },
  { filename: 'uppsala-falhagen.jpg', prompt: `Fålhagen in Uppsala, Sweden, diverse residential neighborhood, mix of old and new buildings, close to city center. ${STYLE}` },
  { filename: 'uppsala-gottsunda.jpg', prompt: `Gottsunda in Uppsala, Sweden, multicultural suburb, green spaces, affordable housing, community center. ${STYLE}` },
  { filename: 'uppsala-sunnersta.jpg', prompt: `Sunnersta in Uppsala, Sweden, southern residential area near Fyris river, nature nearby, calm family neighborhood. ${STYLE}` },
  { filename: 'uppsala-savja.jpg', prompt: `Sävja in Uppsala, Sweden, growing residential area, modern apartments, bike paths, close to nature. ${STYLE}` },

  // ─── LINKÖPING NEIGHBORHOODS ─────────────────────────────────
  { filename: 'linkoping-centrum.jpg', prompt: `Linköping city center, Sweden, Stora Torget square, shopping streets, cathedral area, typical Swedish medium city. ${STYLE}` },
  { filename: 'linkoping-berga.jpg', prompt: `Berga neighborhood in Linköping, Sweden, modern suburban area, residential houses and apartments, green spaces. ${STYLE}` },
  { filename: 'linkoping-ryd.jpg', prompt: `Ryd student area in Linköping, Sweden, near university campus, student housing, young atmosphere. ${STYLE}` },
  { filename: 'linkoping-lambohov.jpg', prompt: `Lambohov in Linköping, Sweden, residential suburb, family houses, parks, Swedish suburban living. ${STYLE}` },
  { filename: 'linkoping-ekholmen.jpg', prompt: `Ekholmen in Linköping, Sweden, residential area near lake, apartment buildings, green surroundings. ${STYLE}` },
  { filename: 'linkoping-tannefors.jpg', prompt: `Tannefors in Linköping, Sweden, historic industrial area turned residential, Kinda Canal, charming neighborhood. ${STYLE}` },
  { filename: 'linkoping-hjulsbro.jpg', prompt: `Hjulsbro in Linköping, Sweden, southern suburb, villa area, family-friendly, near Stångån river. ${STYLE}` },
  { filename: 'linkoping-tornby.jpg', prompt: `Tornby in Linköping, Sweden, commercial area with shops, modern development, northern part of city. ${STYLE}` },

  // ─── SMALLER CITIES (centrum + residentiel) ──────────────────
  { filename: 'helsingborg-centrum.jpg', prompt: `Helsingborg city center, Sweden, pedestrian streets, Kärnan tower visible, shops and cafes, Öresund coast city. ${STYLE}` },
  { filename: 'helsingborg-residentiel.jpg', prompt: `Residential neighborhood in Helsingborg, Sweden, charming villas, tree-lined streets, Swedish south coast living. ${STYLE}` },
  { filename: 'jonkoping-centrum.jpg', prompt: `Jönköping city center, Sweden, lakefront promenade, shops, Lake Vättern views, typical Swedish Småland city. ${STYLE}` },
  { filename: 'jonkoping-residentiel.jpg', prompt: `Residential area in Jönköping, Sweden, family houses near lake, green gardens, peaceful Småland living. ${STYLE}` },
  { filename: 'lund-centrum.jpg', prompt: `Lund city center, Sweden, university quarter, Lund Cathedral, academic bookshops, cobblestone streets, students on bikes. ${STYLE}` },
  { filename: 'lund-residentiel.jpg', prompt: `Residential Lund, Sweden, charming student housing, small gardens, quiet academic town atmosphere. ${STYLE}` },
  { filename: 'gavle-centrum.jpg', prompt: `Gävle city center, Sweden, historic wooden buildings, pedestrian area, Gavleån river bridges. ${STYLE}` },
  { filename: 'gavle-residentiel.jpg', prompt: `Residential neighborhood in Gävle, Sweden, traditional Swedish houses, quiet streets, northern Norrland feel. ${STYLE}` },
  { filename: 'boras-centrum.jpg', prompt: `Borås city center, Sweden, street art sculptures, textile heritage buildings, modern Swedish city. ${STYLE}` },
  { filename: 'boras-residentiel.jpg', prompt: `Residential area in Borås, Sweden, Swedish houses with gardens, family neighborhood, west Sweden inland. ${STYLE}` },
  { filename: 'eskilstuna-centrum.jpg', prompt: `Eskilstuna city center, Sweden, Fristaden shopping area, river walk, industrial heritage buildings. ${STYLE}` },
  { filename: 'eskilstuna-residentiel.jpg', prompt: `Residential Eskilstuna, Sweden, typical Swedish suburban houses, gardens, parks, Sörmland region. ${STYLE}` },
  { filename: 'norrkoping-centrum.jpg', prompt: `Norrköping city center, Sweden, industrial landscape rapids, red brick buildings, unique urban waterfall area. ${STYLE}` },
  { filename: 'norrkoping-residentiel.jpg', prompt: `Residential neighborhood in Norrköping, Sweden, traditional Swedish houses, quiet streets, east Sweden. ${STYLE}` },
  { filename: 'orebro-centrum.jpg', prompt: `Örebro city center, Sweden, Örebro Castle with water moat, Stortorget square, Swedish charm. ${STYLE}` },
  { filename: 'orebro-residentiel.jpg', prompt: `Residential area in Örebro, Sweden, family villas, green neighborhood near Svartån river. ${STYLE}` },
  { filename: 'vasteras-centrum.jpg', prompt: `Västerås city center, Sweden, Stora Torget square, pedestrian shopping, Lake Mälaren city. ${STYLE}` },
  { filename: 'vasteras-residentiel.jpg', prompt: `Residential Västerås, Sweden, lakeside houses, Swedish suburban family living, Mälardalen region. ${STYLE}` },
  { filename: 'umea-centrum.jpg', prompt: `Umeå city center, Sweden, birch-lined Rådhusesplanaden, winter scene, university town in northern Sweden. ${STYLE}` },
  { filename: 'umea-residentiel.jpg', prompt: `Residential Umeå, Sweden, modern apartments, birch trees, northern Swedish city life, snow. ${STYLE}` },
  { filename: 'sundsvall-centrum.jpg', prompt: `Sundsvall stone city center, Sweden, grand 19th century buildings, Storgatan, northern Swedish coast town. ${STYLE}` },
  { filename: 'karlstad-centrum.jpg', prompt: `Karlstad city center, Sweden, Stora Torget with sun statue, Klarälven river, charming Värmland capital. ${STYLE}` },
  { filename: 'vaxjo-centrum.jpg', prompt: `Växjö city center, Sweden, cathedral, Växjösjön lake, green Småland city, sustainable architecture. ${STYLE}` },
  { filename: 'halmstad-centrum.jpg', prompt: `Halmstad city center, Sweden, Nissan river, castle, pedestrian streets, Swedish Halland coast town. ${STYLE}` },

  // ─── GUIDE IMAGES ────────────────────────────────────────────
  { filename: 'guide-stockholm.jpg', prompt: `Stockholm, Sweden overview photo for a guide, showing Gamla Stan, water, bridges, Swedish flag, summer. ${STYLE}` },
  { filename: 'guide-personnummer.jpg', prompt: `Swedish personal number (personnummer) concept, Skatteverket office exterior, Swedish administrative documents, ID card. ${STYLE}` },
];

// ============================================================
// DOWNLOAD + GENERATE FUNCTIONS
// ============================================================

function downloadImage(url, filepath) {
  return new Promise((resolve, reject) => {
    const protocol = url.startsWith('https') ? https : http;
    protocol.get(url, (response) => {
      if (response.statusCode === 301 || response.statusCode === 302) {
        return downloadImage(response.headers.location, filepath).then(resolve).catch(reject);
      }
      const fileStream = fs.createWriteStream(filepath);
      response.pipe(fileStream);
      fileStream.on('finish', () => { fileStream.close(); resolve(); });
      fileStream.on('error', reject);
    }).on('error', reject);
  });
}

async function generateImage(img, index, total) {
  const filepath = path.join(IMAGES_DIR, img.filename);

  // Skip if already exists
  if (fs.existsSync(filepath)) {
    console.log(`[${index + 1}/${total}] SKIP (exists): ${img.filename}`);
    return;
  }

  const size = img.size || '1024x1024';
  console.log(`[${index + 1}/${total}] Generating: ${img.filename} (${size})...`);

  try {
    const response = await openai.images.generate({
      model: 'dall-e-3',
      prompt: img.prompt,
      n: 1,
      size: size,
      quality: img.quality || 'standard',
      response_format: 'url'
    });

    const imageUrl = response.data[0].url;
    await downloadImage(imageUrl, filepath);
    console.log(`[${index + 1}/${total}] OK: ${img.filename}`);
  } catch (error) {
    console.error(`[${index + 1}/${total}] ERROR: ${img.filename} - ${error.message}`);
  }

  // Rate limit: wait 1.5s between requests
  await new Promise(r => setTimeout(r, 1500));
}

async function main() {
  console.log(`\n=== Generating ${images.length} Swedish images ===\n`);

  if (!fs.existsSync(IMAGES_DIR)) {
    fs.mkdirSync(IMAGES_DIR, { recursive: true });
  }

  for (let i = 0; i < images.length; i++) {
    await generateImage(images[i], i, images.length);
  }

  console.log('\n=== Done! ===\n');
}

main();
