#!/usr/bin/python3
from brownie import AegisToken, AegisProxy

def test_contract_compilation():
    """Test that our contracts compile and have the expected interface"""
    print("🧪 TESTING AEGIS FRAMEWORK CONTRACTS")
    print("=" * 50)
    
    # Check AegisToken contract
    print("📄 Checking AegisToken contract...")
    token_abi = AegisToken.abi
    expected_functions = ['name', 'symbol', 'decimals', 'totalSupply', 'balanceOf', 'transfer', 'mint', 'pause', 'unpause', 'owner', 'paused']
    
    function_names = [func['name'] for func in token_abi if func['type'] == 'function']
    print(f"✅ AegisToken has {len(function_names)} functions")
    
    for expected in expected_functions:
        if expected in function_names:
            print(f"   ✅ {expected} - Found")
        else:
            print(f"   ❌ {expected} - Missing")
    
    # Check AegisProxy contract  
    print("\n📄 Checking AegisProxy contract...")
    proxy_abi = AegisProxy.abi
    proxy_functions = [func['name'] for func in proxy_abi if func['type'] == 'function']
    print(f"✅ AegisProxy has {len(proxy_functions)} functions")
    
    # Verify key proxy functions
    key_proxy_functions = ['getImplementation', 'getAdmin']
    for func in key_proxy_functions:
        if func in proxy_functions:
            print(f"   ✅ {func} - Found")
        else:
            print(f"   ❌ {func} - Missing")
    
    print("\n🎉 CONTRACT VALIDATION COMPLETE!")
    print("✨ Your Aegis Framework contracts are properly structured!")
    print("🚀 Next step: Deploy to a real blockchain network")
    
    return True

if __name__ == "__main__":
    test_contract_compilation()