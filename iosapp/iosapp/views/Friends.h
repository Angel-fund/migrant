//
//  Friends.h
//  iosapp
//
//  Created by comger on 13-8-30.
//  Copyright (c) 2013年 comger. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface Friends : UIViewController<UITableViewDataSource,UITableViewDelegate>

@property (nonatomic, retain) NSMutableArray *datalist;
@property (nonatomic, retain) UITableView *table;

@end
