import time
import requests
from rich.console import Console
from rich.table import Table

console = Console()

# Lista de hosts que vamos monitorar
SITES = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.cloudflare.com",
    "https://site-com-erro-exemplo.com"  # Exemplo para testar site offline
]

def verificar_sites():
    table = Table(title="📡 Monitor de Status de Serviços")

    table.add_column("URL / Serviço", style="cyan")
    table.add_column("Status", justify="center")
    table.add_column("Tempo de Resposta", justify="right")

    for url in SITES:
        try:
            inicio = time.time()
            resposta = requests.get(url, timeout=3)
            tempo_ms = round((time.time() - inicio) * 1000, 2)

            if resposta.status_code == 200:
                table.add_row(url, "[bold green]ONLINE[/bold green]", f"{tempo_ms} ms")
            else:
                table.add_row(url, f"[bold yellow]HTTP {resposta.status_code}[/bold yellow]", f"{tempo_ms} ms")

        except requests.RequestException:
            table.add_row(url, "[bold red]OFFLINE / ERRO[/bold red]", "-")

    console.clear()
    console.print(table)

if __name__ == "__main__":
    verificar_sites()