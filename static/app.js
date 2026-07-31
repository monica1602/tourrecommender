/**
 * TourGuide - JavaScript do Frontend
 * Gerencia filtros, chamadas à API e renderização dos resultados.
 */

document.addEventListener("DOMContentLoaded", () => {
    const paisSelect = document.getElementById("pais");
    const cidadeSelect = document.getElementById("cidade");
    const tipoSelect = document.getElementById("tipo");
    const precoMax = document.getElementById("preco_max");
    const duracaoMax = document.getElementById("duracao_max");
    const pessoasInput = document.getElementById("pessoas");
    const gratuitoCheck = document.getElementById("gratuito");
    const filterForm = document.getElementById("filterForm");
    const btnLimpar = document.getElementById("btnLimpar");
    const resultsGrid = document.getElementById("resultsGrid");
    const resultsCount = document.getElementById("resultsCount");
    const noResults = document.getElementById("noResults");
    const loading = document.getElementById("loading");
    const resultsSection = document.getElementById("resultsSection");

    // Inicializar dados dos selects
    carregarPaises();
    carregarTipos();

    // Carregar todos os passeios ao iniciar
    buscarPasseios();

    // Eventos
    filterForm.addEventListener("submit", (e) => {
        e.preventDefault();
        buscarPasseios();
    });

    paisSelect.addEventListener("change", () => {
        carregarCidades(paisSelect.value);
    });

    btnLimpar.addEventListener("click", limparFiltros);

    // Desabilitar preço quando "gratuito" está marcado
    gratuitoCheck.addEventListener("change", () => {
        precoMax.disabled = gratuitoCheck.checked;
        if (gratuitoCheck.checked) {
            precoMax.value = "";
        }
    });

    // === FUNÇÕES DE CARREGAMENTO ===

    async function carregarPaises() {
        try {
            const resp = await fetch("/api/paises");
            const paises = await resp.json();
            paisSelect.innerHTML = '<option value="">Todos os países</option>';
            paises.forEach((pais) => {
                const opt = document.createElement("option");
                opt.value = pais;
                opt.textContent = pais;
                paisSelect.appendChild(opt);
            });
        } catch (err) {
            console.error("Erro ao carregar países:", err);
        }
    }

    async function carregarCidades(pais) {
        try {
            let url = "/api/cidades";
            if (pais) {
                url += `?pais=${encodeURIComponent(pais)}`;
            }
            const resp = await fetch(url);
            const cidades = await resp.json();
            cidadeSelect.innerHTML = '<option value="">Todas as cidades</option>';
            cidades.forEach((cidade) => {
                const opt = document.createElement("option");
                opt.value = cidade;
                opt.textContent = cidade;
                cidadeSelect.appendChild(opt);
            });
        } catch (err) {
            console.error("Erro ao carregar cidades:", err);
        }
    }

    async function carregarTipos() {
        try {
            const resp = await fetch("/api/tipos");
            const tipos = await resp.json();
            tipoSelect.innerHTML = '<option value="">Todos os tipos</option>';
            tipos.forEach((tipo) => {
                const opt = document.createElement("option");
                opt.value = tipo;
                opt.textContent = tipo;
                tipoSelect.appendChild(opt);
            });
        } catch (err) {
            console.error("Erro ao carregar tipos:", err);
        }
    }

    // === BUSCA DE PASSEIOS ===

    async function buscarPasseios() {
        mostrarLoading(true);
        mostrarNoResults(false);
        resultsGrid.innerHTML = "";

        const filtros = {
            pais: paisSelect.value,
            cidade: cidadeSelect.value,
            tipo: tipoSelect.value,
            gratuito: gratuitoCheck.checked,
            preco_max: parseFloat(precoMax.value) || 0,
            duracao_max: parseInt(duracaoMax.value) || 0,
            pessoas: parseInt(pessoasInput.value) || 0,
        };

        try {
            const resp = await fetch("/api/recomendar", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(filtros),
            });

            const data = await resp.json();
            mostrarLoading(false);

            if (data.passeios.length === 0) {
                mostrarNoResults(true);
                resultsCount.textContent = "";
            } else {
                resultsCount.textContent = `${data.total} passeio${data.total > 1 ? "s" : ""} encontrado${data.total > 1 ? "s" : ""}`;
                renderizarPasseios(data.passeios);
            }

            // Scroll suave até os resultados
            resultsSection.scrollIntoView({ behavior: "smooth", block: "start" });
        } catch (err) {
            console.error("Erro ao buscar passeios:", err);
            mostrarLoading(false);
            mostrarNoResults(true);
        }
    }

    // === RENDERIZAÇÃO ===

    function renderizarPasseios(passeios) {
        resultsGrid.innerHTML = "";

        passeios.forEach((passeio) => {
            const card = document.createElement("div");
            card.className = "tour-card";

            const precoHtml = passeio.gratuito
                ? '<span class="tour-card-price free">Gratuito</span>'
                : `<span class="tour-card-price">R$ ${passeio.preco.toFixed(2)}</span>`;

            const badgeHtml = passeio.gratuito
                ? '<span class="tour-card-badge">Grátis</span>'
                : "";

            const estrelas = "⭐".repeat(Math.round(passeio.avaliacao));

            card.innerHTML = `
                <img class="tour-card-image"
                     src="${passeio.imagem}"
                     alt="${passeio.nome}"
                     loading="lazy"
                     onerror="this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%22400%22 height=%22200%22><rect fill=%22%23e2e8f0%22 width=%22400%22 height=%22200%22/><text x=%2250%25%22 y=%2250%25%22 text-anchor=%22middle%22 dy=%22.3em%22 font-size=%2220%22 fill=%22%2364748b%22>🌍 Imagem</text></svg>'">
                <div class="tour-card-body">
                    <div class="tour-card-header">
                        <h3 class="tour-card-title">${passeio.nome}</h3>
                        <span class="tour-card-rating">⭐ ${passeio.avaliacao}</span>
                    </div>
                    <p class="tour-card-location">📍 ${passeio.cidade}, ${passeio.pais}</p>
                    <p class="tour-card-desc">${passeio.descricao}</p>
                    <div class="tour-card-tags">
                        <span class="tag tag-tipo">${getIconeTipo(passeio.tipo)} ${passeio.tipo}</span>
                        <span class="tag tag-duracao">⏱️ ${passeio.duracao_horas}h</span>
                        <span class="tag tag-pessoas">👥 Até ${passeio.max_pessoas} pessoas</span>
                    </div>
                    <div class="tour-card-footer">
                        ${precoHtml}
                        ${badgeHtml}
                    </div>
                </div>
            `;

            resultsGrid.appendChild(card);
        });
    }

    function getIconeTipo(tipo) {
        const icones = {
            Cultural: "🏛️",
            Natureza: "🌿",
            Aventura: "🧗",
            Gastronomia: "🍷",
            Romântico: "💕",
        };
        return icones[tipo] || "🎯";
    }

    // === UTILITÁRIOS ===

    function mostrarLoading(show) {
        loading.style.display = show ? "block" : "none";
    }

    function mostrarNoResults(show) {
        noResults.style.display = show ? "block" : "none";
    }

    function limparFiltros() {
        paisSelect.value = "";
        cidadeSelect.innerHTML = '<option value="">Todas as cidades</option>';
        tipoSelect.value = "";
        precoMax.value = "";
        precoMax.disabled = false;
        duracaoMax.value = "";
        pessoasInput.value = "";
        gratuitoCheck.checked = false;

        // Recarregar todas as cidades
        carregarCidades("");

        // Buscar todos os passeios
        buscarPasseios();
    }
});
