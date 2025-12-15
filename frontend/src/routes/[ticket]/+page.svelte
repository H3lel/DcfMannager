<script lang="ts">
  import { page } from '$app/state';
  
  let ticket = page.params.ticket;
  let finance_selector: string;
  let balance_sheet: any = {};

  // ✅ Reactive declarations — these update automatically when balance_sheet changes
  let btn_id:any;
  $: btn_id;
  const get_balance_sheet = async () => {
    console.log("req");
    const res = await fetch("/api/get-balance-sheet", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_query: ticket })
    });
    let dummy = await res.json();
    balance_sheet = JSON.parse(dummy)
    console.log(balance_sheet);
  
  };

  const blc_select = (event: any) => {
    let id = event.target.id;
    btn_id = id;
    if (id === "btn_income_statement") {
      finance_selector = "Income Statement";
    } else if (id === "btn_cash_flow") {
      finance_selector = "Cash Flow";
    } else if (id === "btn_balance_sheet") {
      finance_selector = "Balance Sheet";
      get_balance_sheet();
    }
  };
</script>


<h2>{page.params.ticket}</h2>
<!-- <pre>{JSON.stringify(balance_sheet, null, 2)}</pre> -->
<div class="grid md:grid-cols-2 md:grid-rows-3 gap-4 sm:grid-cols-1 sm:grid-rows-3 m-4">
    <div class="container bg-primary-950 md:row-span-55 rounded-3xl p-3">
        <h2 class="h3 font-bold mt-2 text-center">{ticket} | {finance_selector}</h2>
        <hr class="hr border-white my-2">
        <div class="grid grid-cols-3 grid-rows-1">
            <button class="m-1 bg-primary-800 hover:bg-secondary-800 rounded-2xl" id="btn_income_statement" on:click={blc_select}>Income Statement</button>
            <button class="m-1 bg-primary-800 hover:bg-secondary-800 rounded-2xl" id="btn_cash_flow" on:click={blc_select}>Cash Flow</button>
            <button class="m-1 bg-primary-800 hover:bg-secondary-800 rounded-2xl" id="btn_balance_sheet" on:click={blc_select}>Balance Sheet</button>
        </div>
        <hr>
        {#if btn_id == "btn_balance_sheet"}
        <table>
          <thead>
            <tr>
              <th>    </th>
            {#each Object.entries(balance_sheet) as [date, val]}
              <th class="mx-2 p-2">{date}</th>
            {/each}
            </tr> 
            
          </thead>
          <tbody>
            {#if balance_sheet && Object.keys(balance_sheet).length}
              {#each Object.keys(Object.values(balance_sheet)[0] as object) as account}
                <tr>
                  <td class="p-2 font-semibold">{account}</td>

                  {#each Object.values(balance_sheet) as year}
                    {@const y = year as Record<string, number | null>}
                    <td class="p-2 text-right">
                      {y[account] ?? "-"}
                    </td>
                  {/each}
                </tr>
              {/each}
            {/if}
          </tbody>
        </table>  
      {/if}  
      {#if btn_id == "btn_cash_flow"}
        <div>not built yet :3</div>
      {/if} 
    </div>
    <div class="container bg-primary-950 md:row-span-25 rounded-3xl p-3"></div>
    <div class="container bg-primary-950 md:row-span-30 rounded-3xl p-3"></div>

</div>