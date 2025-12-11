<script lang="ts">
    import { tick } from "svelte";

    let timeout: any;
    let ticket_data:any;
   
    const get_ticket_data = async (event: any) => {
        clearTimeout(timeout);

        const value = event.target.value;

        timeout = setTimeout(async () => {
            if (!value) {
                ticket_data = null;
                return;
            }

            const res = await fetch("/api/get-ticker", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ user_query: value })
            });

            ticket_data = await res.json();
        }, 300); 
    };

</script>
<main class="p-8 max-w-3xl mx-auto ">
    <h1 class="text-3xl font-bold mb-6 text-center">Search Market</h1>

    <div class="flex flex-col items-center w-full">
        <div class="w-full md:w-2/3 bg-surface-50 dark:bg-surface-800 rounded-2xl p-6 shadow-lg">

            <!-- Input -->
            <input 
                type="text"
                class="w-full border border-primary-500 rounded-xl p-3 mb-4 focus:ring-2 focus:ring-primary-400 outline-none"
                placeholder="Search ticker symbol..."
                on:input={get_ticket_data}
            />

            <!-- Results -->
            {#if ticket_data}
                <div class="space-y-3">
                    {#each ticket_data as tick}
                        <a href="/{tick.symbol}" class="block">
                            <div class="p-4 rounded-xl bg-surface-100 dark:bg-surface-700 hover:bg-primary-600 hover:text-white transition">
                                <p class="font-semibold text-lg text-primary-500">{tick.symbol}</p>
                                <p class="text-sm opacity-80">{tick.longname}</p>
                                <p class="text-sm opacity-70">{tick.industry}</p>
                            </div>
                        </a>
                    {/each}
                </div>
            {/if}

            <!-- Divider -->
            <hr class="my-6 border-primary-700/20">

            <!-- Last DCF -->
            <div>
                <h2 class="text-xl font-semibold">Last DCF Submitted</h2>
            </div>

        </div>
    </div>
</main>



