import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Service-card.component.html',
  styleUrls: ['./Service-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Service-card]': 'true'
  }
})

export class ServiceCardComponent {


}