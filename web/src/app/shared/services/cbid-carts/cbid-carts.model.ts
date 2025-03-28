export class CbidCart {
  public id: string;
  public search_criteria: string;
  public total_pages: string;
  public total_company: string;
  public unit_price: string;
  public total_price: string;
  public total: string;
  public sst: string;
  public total_amount: string;
  public date_created: string;
  public date_modified: string;
  public products: string;
  public entity_type: string;
  public product_type: string;

  constructor(
    id: string,
    total_pages: string,
    search_criteria: string,
    total_company: string,
    unit_price: string,
    total_price: string,
    total: string,
    sst: string,
    total_amount: string,
    date_created: string,
    date_modified: string,
    products: string,
    entity_type: string,
    product_type: string
  ) {
    this.id = id;
    this.total_pages = total_pages;
    this.search_criteria = search_criteria;
    this.total_company = total_company;
    this.unit_price = unit_price;
    this.total_price = total_price;
    this.total = total;
    this.sst = sst;
    this.total_amount = total_amount;
    this.date_created = date_created;
    this.date_modified = date_modified;
    this.products = products;
    this.entity_type = entity_type;
    this.product_type = product_type;
  }
}
