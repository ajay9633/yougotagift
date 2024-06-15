/** @odoo-module */
import { useService } from "@web/core/utils/hooks";
const { Component, onWillStart } = owl;

export class PurchaseDashBoard extends Component {
    /**
     * Setup method for initializing the component.
     */
    setup() {
        // Get references to Odoo services
        this.orm = useService("orm");
        this.action = useService("action");

        onWillStart(async () => {
            this.purchaseData = await this.orm.call(
                "purchase.order",
                "get_dashboard_values"
            );
        });
    }

    setSearchContext(ev) {
        let filter_name = ev.currentTarget.getAttribute("filter_name");
        let filters = filter_name.split(',');

        let searchItems = this.env.searchModel.getSearchItems((item) => filters.includes(item.name));

        this.env.searchModel.query = [];

        // Activate filters in the search model
        for (const item of searchItems) {
            this.env.searchModel.toggleSearchItem(item.id);
        }
    }
}

PurchaseDashBoard.template = 'yg_purchase_dashboard.PurchaseDashboard';
